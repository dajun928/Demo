# -*- coding:utf-8 -*-
#待解决
# tasks.py
import time
from celery import Celery

app = Celery('hello', broker='redis://localhost:6379')
from celery import Celery

app = Celery('TASK',broker='redis://localhost',
             backend='redis://localhost')


@app.task
def add(x, y):
    print("running...", x, y)
    return x + y