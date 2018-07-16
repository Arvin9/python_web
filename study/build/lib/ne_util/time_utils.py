# -*- coding:utf-8 -*-
import datetime

def current_time(days=0):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days)
    now = now + delta
    return now.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print(current_time())