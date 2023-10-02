import utils.loggers as loggers

from client.handlers import *
from db.config import SESSION_NAME, API_ID, API_HASH
from telethon import TelegramClient, events, functions


# Authenticate client
client = TelegramClient("sessions/" + SESSION_NAME, API_ID, API_HASH)
loggers.client.info("User is authenticated.")

# Adding handlers


@client.on(events.UserUpdate)
async def user_update(event):
    await user_update_handler(client, event)


async def main():
    try:
        async with client:
            # Starting client
            loggers.client.info("User is started.")
            await client.run_until_disconnected()
    except KeyboardInterrupt:
        # Safe disconnect
        client.disconnect()
        loggers.client.info("Client disconnected.")
