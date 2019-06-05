#!/usr/bin/env python
# encoding: utf-8
import time


def hello():
    time.sleep(1)


def run():
    for i in range(5):
        hello()
        print('Hello World:%s' % time.time())


if __name__ == '__main__':
    run()
