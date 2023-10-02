import datetime as dt


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
