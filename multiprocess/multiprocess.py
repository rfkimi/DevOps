#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process name:', os.getppid())  # 打印父进程
    print('child process name:', os.getpid())  # 打印子进程


def f(name):
    info('\033[31;1m called from child process function f \033[0m')  # 打印f函数的父子进程
    print'hello ' + name


def run(name):
    print name + ' ' + 'process create!'


if __name__ == '__main__':
    info('\033[32;1m main process \033[0m')
    p = Process(target=f, args=('test1',))  # 创建进程实例
    p.start()
    p.join()
