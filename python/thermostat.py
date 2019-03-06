import random
import datetime

def get_temperature():
    now = datetime.datetime.now()
    minute = now.minute

    if minute < 20:
        temp = minute + now.second/10
    elif minute < 40:
        temp = (40 - minute) - now.second/10
    elif minute < 60:
        temp = (60 - minute) - now.second/10

    return temp
