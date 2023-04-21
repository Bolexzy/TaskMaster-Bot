"""Defines a temporary mail generator."""

import requests
import hashlib
import random
import string
from sys import argv, exit
import pyperclip
import time
import datetime
import os
import json
from typing import List, Dict

API_KEY = "Your token here"

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request"
headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
    }


def domains_list() -> List[str]:
    """
    Get the list of domains (JSON).

    Returns:
        List[str]: List of domains as strings.
    """
    d_url = f"{url}/domains/"

    response = requests.get(d_url, headers=headers)
    return json.loads(response.text)


def generate_username() -> str:
    """
    Generates a new email username of length 7.

    Returns:
        str: Generated username string.
    """
    name = string.ascii_lowercase + string.digits
    return ''.join(random.choice(name) for i in range(7))


def get_temp_email(user_name=None) -> str:
    """Generate a temporary email with a random username and domain."""
    if user_name is None:
        user_name = generate_username()
    # generate domain name
    domains = domains_list()
    domain = random.choice(domains).strip('"')

    if not user_name.isalnum():
        return ("Invalid input. Please enter a string of lowercase\
                    letters and numbers only.")
    new_mail = f"{user_name}{domain}"
    return (f"\nYour temporary email is {new_mail}\
                (Copy Email address and save.)\n")


def check_temp_email(mail: str) -> str:
    """
    Check and get a list of emails for a mailbox.

    Args:
        mail (str): Email address to check.
    Returns:
        str: A string containing the sender, recipient, subject, date,
        and content of the latest email.
        If no email is found, returns "No emails yet.".
        If there's an error, returns "Failed to decode JSON response."

    Raises:
        requests.exceptions.RequestException:
        If there's an error making the HTTP request.

    """

    # hash mail using md5
    md5_hash = hashlib.md5(mail.encode()).hexdigest()
    id_hash = md5_hash

    # request url
    mail_url = f"{url}/mail/id/{id_hash}"

    try:
        # Get emails
        response = requests.get(mail_url, headers=headers)
        response.raise_for_status()  # raise an exception if there's an error in the HTTP response

        # parse response
        data = json.loads(response.text)

        if data:
            # Extract mail_from,mail_subject,mail_content,mail_date
            # + from the first item in the list
            latest_email = data[0]
            mail_from = latest_email.get("mail_from", "")
            mail_subject = latest_email.get("mail_subject", "")
            mail_content = latest_email.get("mail_text_only", "")
            mail_date = latest_email.get("mail_timestamp", 0)
            date = datetime.datetime.fromtimestamp(mail_date).strftime('%Y%m%d')

            # Construct the email message
            email_message = (f"Sender: {mail_from}\n"
                             f"To: {mail}\n"
                             f"Subject: {mail_subject}\n"
                             f"Date: {date}\n"
                             f"------------------------------------\n\n"
                             f"Content: {mail_content}\n")

            return email_message
        else:
            return "No emails yet."
    except requests.exceptions.RequestException as e:
        # If there's an error making the HTTP request
        print(f"An error occurred while trying to check email: {e}")
        raise e
    except Exception as e:
        # If there's any other error
        if "There are no emails yet" in response.text:
            return ("No emails yet.")
        print(f"An error occurred while trying to check email: {e}")


if __name__ == "__main__":
    try:
        domains = domains_list()
        domain = random.choice(domains).strip('"')
        if len(argv) > 1 and argv[1] == 'Y':
            user_input = input("\nEnter youre preferred mail username: ")
            if user_input.isalnum():
                user_input = user_input.lower()
            else:
                print("Invalid input. Please enter a string of lowercase\
                        letters and numbers only.")
                exit(1)  # Exit with error code 1
            new_mail = f"{user_input}{domain}"
        else:
            new_mail = f"{generate_username()}{domain}"
            # pyperclip.copy(mail)
        print(f"\nYour temporary email is {new_mail}\
                (Email address copied to clipboard.)\n")
        print(f"------------ | Inbox of {new_mail} | ------------\n")
        while True:
            check_mail(new_mail)
            time.sleep(5)

    except Exception as e:
        print("\nEncountered an error")
        print(e)
