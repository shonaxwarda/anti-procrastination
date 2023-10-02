from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from bot.models import Bot
from db.config import WORK_DAY_END
from db.wrapper import DBWrap
from utils import loggers


async def testing():
    loggers.root.info('exec')


async def scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(DBWrap().reset_db, 'cron', hour=0, minute=0)
    scheduler.add_job(Bot().send_today_online_time, 'cron',
                      hour=int(WORK_DAY_END.split(':')[0]),
                      minute=int(WORK_DAY_END.split(':')[1]))
    scheduler.add_job(Bot().send_today_online_time, 'cron', hour=0, minute=0)
    scheduler.start()

    try:
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
