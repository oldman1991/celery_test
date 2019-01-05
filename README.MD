# 项目说明
## 启动方式
1.  `celery worker -A celery_test -l debug`
    -l: 日志的等级，和logging模块的等级一样，只有等级大于等于该参数的日志才会被打印输出出来
    -Q: 指定启动的队列，如果不指定，则启动默认配置在CELERY_QUEUES参数里面的队列

## celery的一些说明
1. celery使用redis做消息队列的时间，如果队列里面没有任务，则队列也会自动的被删除，所以keys *的时间是看不到这个list的key

## 项目说明
1.  `test.testdemo1`
    celery的一些正常的调用，包括一些参数的使用

