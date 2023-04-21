# TaskMaster Bot [![Join on Telegram](https://img.shields.io/badge/Chat%20On%20-Telegram-blue.svg)]

This is a Telegram bot designed to test various unit projects. It has several functionalities such as creating temporary emails and checking for new emails.


## Demo

Insert gif or link to demo


## Installation

To run this bot, you will need to install Python 3 and the necessary dependencies. 

```bash
 pip install -r requirements.txt
```
You will also need to set the environment variables for your bot token and other necessary variables.
## Usage/Examples
To start the bot, run the following command:

```bash
python3 main.py
```
You can then interact with the bot on Telegram by sending messages to it.

### Greetings
**[hello, hi, wassup]**: The bot will respond with "Hello there!".

### Bot Info
**[who are you?, who are you**]: The bot will introduce itself as "TaskMaster bot".

### Date and Time
**[time, time?, date]**: The bot will respond with the current date and time.

### Temporary Email
**[create email]**: The bot will generate a temporary email address for you to use. If a username is specified, it will be used as part of the email address. 
#### Example: *"create email john"* will generate an email address such as "john@abc.com". If no username is specified, a random username will be generated instead. The email provider is "tempmail".

**[check email]**: The bot will check for new emails received at the temporary email address generated. Note that this feature uses a third-party API (https://temp-mail.org/en/api/) and may be subject to rate limiting or other usage restrictions.
## Contribution & Support

- Please ⭐️ this repository if this project helped you!
- 3Contributions are always welcome!

Please adhere to this project's `code of conduct`.


## License
TaskMaster Bot is made  by [@Bolexzy](https://twitter.com/Bolexzyy__) and it is released under the MIT license.

[MIT](https://choosealicense.com/licenses/mit/)


