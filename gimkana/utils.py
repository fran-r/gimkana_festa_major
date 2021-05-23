from datetime import datetime

from django.shortcuts import redirect

from .constants import START_DATETIME, END_DATETIME


def is_started():
    print(datetime.now())
    print(START_DATETIME)
    return START_DATETIME < datetime.now()


def is_finished():
    return END_DATETIME < datetime.now()


def redirect_not_started():
    return redirect('not-started')
