from aiogram import Bot as b
from db.config import BOT_TOKEN, OBSERVABLE_USER
from utils.utils import get_current_time
import utils.loggers as loggers


class Bot():
    def __init__(self):
        self.BOT_TOKEN = BOT_TOKEN
        self.bot = b(self.BOT_TOKEN)

    async def online_detected(self):
        loggers.bot.info("detected online.")
        await self.bot.send_message(OBSERVABLE_USER, f"""
    ⚠️ You are online again. <b>Please refrain from procrastination and continue to work.</b>

Current time: {get_current_time()} 
    """, parse_mode="HTML")
