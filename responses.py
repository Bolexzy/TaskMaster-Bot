from datetime import datetime
from temp_mail import *


def sample_responses(input_text: str) -> str:
    """
    Generate a response to a user input message.

    Args:
        input_text (str): The user input message.

    Returns:
        str: The response to the user input message.
    """
    user_message = str(input_text).lower()

    if user_message in ['hello', 'hi', 'wassup']:
        return "Hello there!"

    if user_message in ['who are you?', 'who are you']:
        return "I am TaskMaster bot"

    if user_message in ['time', 'time?', 'date']:
        date_now = datetime.now()
        date_time = date_now.strftime("%d/%m/%y %H:%M:%S")

        return(str(date_time))

    if "create email" in user_message:
        text_list = user_message.split(' ')
        if len(text_list) > 2:
            email = get_temp_email(text_list[2])
        else:
            email = get_temp_email()
        if "error" in email:
            return "Sorry, an error occurred while generating\
                    a temporary email. Please try again later."
        return f"Your temporary email is {email}"

    if "check email" in user_message:
        text_list = user_message.split(' ')
        if len(text_list) > 2:
            emails = check_temp_email(text_list[2])
        else:
            emails = check_temp_email()
        if "error" in emails:
            return "Sorry, an error occurred while generating\
                    a temporary email. Please try again later."
        return f"You have {len(emails)} new emails\n\n{emails}"

    return ("Unable to process your message")
