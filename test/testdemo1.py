# coding=utf-8
# create by oldman at 17/7/14
import logging
from _celery import app

from celery_test.logger import info_logger


@app.task(bind=True)
def add(self,x, y):
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
    测试使用apply_async方法。
    指定使用的队列queue
    等待一段时间后再执行 countdown，单位是s
    指定任务开始执行时间 eta ，这个是UTC时间
    设置超时时间 expires 单位是s
    :return:
    """
    add.apply_async((1,3),queue='add')



add.delay(2,3)
# add.delay(3,4)