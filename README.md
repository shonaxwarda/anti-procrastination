# Anti-procrastination via Telegram

Many people suffer from procrastination when they try to work or do something useful.

Here comes this script that will help you to work and count how much time have you **wasted** on telegram.

## Installation

### Bot

- Create new bot via [BotFather](https://t.me/BotFather)
- Replace existing token in config file

### Client

- Create new folder `sessions` in root directory of script
- Create new app at https://my.telegram.org and save api_id, api_hash to config file
- Login via Telegram (use your second account or create a new one)
- Insert your username `@durov` into the config file
- Open last activity to your second account `via privacy settings`
- Done!

### Config file

- Replace your working hours with existing ones in config file

### Starting

- `pip install -r requirements.txt` - install all requirements
- `python3 main.py` - linux/mac ; `python main.py` - windows

## Additional information

Script will not steal your Telegram session, it is stored **locally**.
