#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/20


from __future__ import  absolute_import, unicode_literals
import sys
from kombu import Connection, Producer, Exchange

def main(arguments):
    exchange = Exchange('kombu_demo', type='direct')
    with Connection("redis://127.0.0.1:6379") as conn:
        producer = Producer(conn)
        producer.publish({'hello': 'world'},
                         exchange=exchange,
                         routing_key='kombu_demo',
                         serializer='json', compression='zlib')

if __name__== "__main__":
    sys.exit(main(sys.argv[1:]))