#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/20


from __future__ import absolute_import, unicode_literals
import sys
from kombu import Connection

def main(arguments):
    with Connection('redis://127.0.0.1:6379') as conn:
        with conn.SimpleQueue('kombu_demo') as queue:
            message = queue.get(block=True, timeout=10)
            message.ack()
            print(message.payload)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))