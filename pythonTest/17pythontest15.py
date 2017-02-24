#!/usr/bin/python3

#import datetime
from datetime import datetime,timedelta

def getyesterday():
    now=datetime.now()

    #datetime.timedelta表示时间间隔，即两个时间点之间的长度
    oneday=timedelta(days=1,hours=1)
    yesterday=now-oneday
    return yesterday

print(getyesterday())
