# 项目说明
## 启动方式
1.  `celery worker -A celery_test -l debug`

    -l: 日志的等级，和logging模块的等级一样，只有等级大于等于该参数的日志才会被打印输出出来

    -Q: 指定启动的队列，如果不指定，则启动默认配置在CELERY_QUEUES参数里面的队列
    -A：指定的celery的名字，在你定义celery的时候定义的，这个项目定义的是'celery_test'

## celery的一些说明
1. celery使用redis做消息队列的时间，如果队列里面没有任务，则队列也会自动的被删除，所以keys *的时间是看不到这个list的key
2. redis里面的unacked是一个hash，会记录所有接收到的但是还没有执行的任务。
3. celery加载的任务通过app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)来配置，默认会把APPS下面的tasks文件夹下的所有的task加载进去，具体的可以查看autodiscover_tasks的方法


## 日志说明
1. 在setting.py 里面 from .log_settings import *，可以使用logging模块写文件日志

## 项目说明
1.  `test.testdemo1`
    celery的一些正常的调用，包括一些参数的使用


