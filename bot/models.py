from aiogram import Bot as b
from db.config import BOT_TOKEN, OBSERVABLE_USER
from db.wrapper import DBWrap
from utils.utils import get_current_time, is_in_work_day
import utils.loggers as loggers


class Bot():
    def __init__(self):
        self.BOT_TOKEN = BOT_TOKEN
        self.bot = b(self.BOT_TOKEN)

    async def online_detected(self):
        loggers.bot.info("detected online.")
        if not is_in_work_day():
            return
        await self.bot.send_message(OBSERVABLE_USER, f"""
    ⚠️ You are online again. <b>Please refrain from procrastination and continue to work.</b>

Current time: {get_current_time()} 
    """, parse_mode="HTML")

    async def send_today_online_time(self):
        today_online_time = DBWrap().get_today_online_time()
        msg = "🕛 Today you have spent following time in Telegram:\n\n"
        msg += get_today_usage_message(today_online_time)

        msg += "\n🏢 At work:"
        today_online_time = DBWrap().get_today_online_work_time()
        msg += get_today_usage_message(today_online_time)

        await self.bot.send_message(OBSERVABLE_USER, msg, parse_mode="HTML")

    def get_today_usage_message(self, today_online_time):
        msg = ""
        hours, minutes, seconds = 0, 0, 0
        if today_online_time >= 60*60:
            hours = today_online_time // (60 * 60)
            today_online_time %= 60 * 60

        if today_online_time >= 60:
            minutes = today_online_time // 60
            today_online_time %= 60

        seconds = today_online_time
        if hours:
            msg += f"<b>Hours:</b> <code>{hours}</code>\n"
        if minutes or hours:
            msg += f"<b>Minutes:</b> <code>{minutes}</code>\n"
        if seconds or minutes or hours:
            msg += f"<b>Seconds:</b> <code>{seconds}</code>\n"

        return msg
