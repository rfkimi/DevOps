#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Queue, Process


def f(cq):
    cq.put(['my', 'name', 'is', ['lilei', 'xixi']])  # 往队列中添加一个元素


if __name__ == '__main__':
    mq = Queue()            # 定义进程队列实例
    mq.put('fome main')     # 往队列中添加一个元素
    p = Process(target=f, args=(mq,))  # 创建一个子进程，并将mq传给子进程
    p.start()                       # 启动
    p.join()                        # 等待子进程执行完毕
    print('444', mq.get_nowait())  # 获取队列元素
    print('444', mq.get_nowait())
