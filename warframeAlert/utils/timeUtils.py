# coding=utf-8
from __future__ import annotations

import datetime
import time
from typing import Tuple

from warframeAlert.services.translationService import translate
from warframeAlert.utils import commonUtils


def get_time(times: int | str) -> str:
    return datetime.datetime.fromtimestamp(int(times[:10])).strftime("%d/%m/%Y %H:%M")


def get_date_time(times: int | str) -> str:
    return datetime.datetime.fromtimestamp(int(times[:10])).strftime("%d/%m/%Y")


def get_alert_time(timer: int | str) -> str:
    if (timer == translate("timeUtils", "Timed Out")):
        return translate("timeUtils", "Timed Out")
    timer = int(timer)
    day = hour = minute = sec = 0
    date = ""
    while (timer > 0):
        if (timer - 86400 >= 0):
            day += 1
            timer -= 86400
            continue
        if (timer - 3600 >= 0):
            hour += 1
            timer -= 3600
            if (hour >= 24):
                hour = 0
                day += 1
            continue
        if (timer - 60 >= 0):
            minute += 1
            timer -= 60
            if (minute >= 60):
                minute = 0
                hour += 1
            continue
        else:
            sec = timer
            timer = 0
    if (day != 0 and day == 1):
        date = date + "1 " + translate("timeUtils", "Day") + " "
    elif (day != 0):
        date = date + str(day) + " " + translate("timeUtils", "Days") + " "
    if (hour != 0):
        date = date + str(hour) + "h "
    if (minute != 0):
        date = date + str(minute) + "m "
    if (str(sec) == "0"):
        return date
    else:
        return date + str(sec) + "s"


def get_local_time() -> str:
    return str(time.mktime(time.localtime()))[0:-2]


def get_earth_time() -> Tuple[int, bool]:
    now = int(time.time())
    cycle_sec = now % 28800  # 8 hours
    day = cycle_sec > 14400
    remaining_sec = 14400 - (cycle_sec % 14400)
    return remaining_sec, day


def get_cetus_time(bounty_end_time) -> Tuple[int, bool]:
    try:
        now = int(time.time())
        remaining_sec = bounty_end_time - now
        day = remaining_sec > 3000

        if (day):
            cycle_remaining_sec = remaining_sec - 3000
        else:
            cycle_remaining_sec = remaining_sec

        return cycle_remaining_sec, day
    except Exception as err:
        commonUtils.print_traceback(translate("timeUtils", "error_get_cetus_time") + ":\n  " + str(err))
        return int(time.time()), False


def get_fortuna_time() -> Tuple[int, bool]:
    try:
        # cold, warm, cold, freeze, 6 minutes and 40 seconds for cycle
        now = int(time.time())
        init_fortuna = 1542131224  # '13/11/2018 18:47' the initial instant of all cycle
        cycle_sec = (now - init_fortuna) % 1600
        heat_moment = 800 < cycle_sec <= 1200
        if (cycle_sec <= 800):
            cycle_sec = 800 - cycle_sec
        elif (heat_moment):
            cycle_sec = 1200 - cycle_sec
        elif (cycle_sec > 1200):
            cycle_sec = 800 + (1600 - cycle_sec)

        return cycle_sec, heat_moment
    except Exception as err:
        commonUtils.print_traceback(translate("timeUtils", "error_get_fortuna_time") + ":\n  " + str(err))
        return int(time.time()), False
