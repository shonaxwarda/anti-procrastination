import logging
import logging.config

logging.basicConfig(format='[%(levelname)5s/%(asctime)s] %(name)s (%(funcName)s): %(message)s',
                    level=logging.INFO)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

bot = logging.getLogger("bot")
client = logging.getLogger("client")
db = logging.getLogger("db")
root = logging.getLogger("root")
