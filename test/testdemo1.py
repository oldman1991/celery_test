# coding=utf-8
# create by oldman at 17/7/14
import logging
from celery import shared_task

from celery_test.logger import info_logger


@shared_task(bind=True)
def add(self, x, y):
    print(self.request.id)
    info_logger.debug(u"i am a bug")
    info_logger.info(u"i am a info")
    return x + y

@shared_task
def test_queue(x, y):
    return x+y

def excute_task():
    test_queue.apply_async((1,3),queue='add')
