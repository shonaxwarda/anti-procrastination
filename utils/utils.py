import datetime as dt
from db.config import WORK_DAY_START, WORK_DAY_END


def get_current_time():
    current_time = dt.datetime.now().time()
    current_time = current_time.strftime("%H:%M:%S")

    return current_time


def get_time_difference(current_time, last_time):
    time_format = "%H:%M:%S"
    time1 = dt.datetime.strptime(current_time, time_format)
    time2 = dt.datetime.strptime(last_time, time_format)

    # Calculate the difference in seconds
    time_difference_seconds = (time1 - time2).total_seconds()

    return time_difference_seconds


def is_in_work_day():
    time_format = "%H:%M:%S"
    work_start = dt.datetime.strptime(WORK_DAY_START, time_format)
    work_end = dt.datetime.strptime(WORK_DAY_END, time_format)
    current_time = dt.datetime.now()
    return work_start < current_time < work_end
