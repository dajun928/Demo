# coding=utf-8

# 定时任务

from apscheduler.schedulers.blocking import BlockingScheduler

from datetime import datetime
from  task import  *
import time
import os


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(fun1, 'cron', hour ='22',minute ='13')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


    # tick()