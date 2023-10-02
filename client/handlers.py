from bot.models import Bot
from datetime import datetime as dt
from db.config import OBSERVABLE_USER
from db.wrapper import DBWrap
from telethon import events, sync
from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline, User
import utils.loggers as loggers
from utils.utils import get_current_time


async def user_update_handler(client: TelegramClient, event: events.UserUpdate):
    """
    Handler for receiving updates on user going online or offline.
    """

    # Filter out other events that are not our current job
    if not isinstance(event.status, UserStatusOffline) and not isinstance(event.status, UserStatusOnline):
        return
    if event.original_update.user_id != OBSERVABLE_USER:
        return

    # Getting user status
    status: str = "online" if isinstance(
        event.status, UserStatusOnline) else "offline"

    # Stopping handler if status is not changed (Telegram can send double online messages)
    if status == DBWrap().get_last_status():
        return

    # Getting current time in HH:MM:SS format
    current_time = get_current_time()

    # Sending notification to user if he is online
    if status == "online":
        await Bot().online_detected()

    # Write to DB
    DBWrap().set_data(status, current_time)

    # logging
    loggers.client.info(
        f"status has been changed to {status}")
