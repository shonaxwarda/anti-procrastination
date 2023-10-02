import json
from utils import loggers
from utils.utils import get_time_difference


class DBWrap():
    with open("db\data.json", 'r') as f:
        _data = json.load(f)

    @classmethod
    def set_data(cls, last_status, last_updated):
        today_online_time = cls._data.get("today_online_time")
        new_data = {
            "last_status": last_status,
            "last_updated": last_updated,
            "today_online_time": today_online_time
        }

        if cls._data.get('last_status') == "online" and last_status == "offline":
            last_updated_old = cls._data.get("last_updated")
            difference = get_time_difference(last_updated, last_updated_old)
            today_online_time += difference
            new_data["today_online_time"] = today_online_time

        cls._data = new_data
        cls.write_on_disk()

    @classmethod
    def write_on_disk(cls):
        with open("db\data.json", 'w') as f:
            f.write(json.dumps(cls._data))

        loggers.db.info("Writing data to disk:", cls._data)

    @classmethod
    def get_last_status(cls):
        return cls._data.get('last_status')

    @classmethod
    def reset_db(cls):
        cls._data = {
            "last_status": "offline",
            "last_updated": "00:00:00",
            "today_online_time": 0
        }
