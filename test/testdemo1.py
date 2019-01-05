# coding=utf-8
# create by oldman at 17/7/14
import logging
from celery import shared_task

from celery_test.logger import info_logger


@shared_task(bind=True)
def add(self, x, y):
    """
    测试bind参数，打印task_id
    调用方式 add.delay(1,2)
    :param self:
    :param x:
    :param y:
    :return:
    """
    print(self.request.id)
    info_logger.debug(u"i am a bug")
    info_logger.info(u"i am a info")
    return x + y


def excute_task():
    """
    测试使用apply_async方法。指定使用的队列
    :return:
    """
    add.apply_async((1,3),queue='add')
