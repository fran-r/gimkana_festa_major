from datetime import datetime

from .constants import START_DATETIME, END_DATETIME


def is_started():
    return START_DATETIME < datetime.now()


def is_finished():
    return END_DATETIME < datetime.now()
