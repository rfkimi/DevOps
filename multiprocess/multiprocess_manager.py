#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Process,Manager
import os


def run(d, l):
    d[os.getpid()] = os.getpid()  # 以当前子进程的pid为key，同时pid也作为value
    l.append(os.getpid())
    print(d, l)


if __name__ == '__main__':
        with Manager() as manager:
            d = manager.dict()  # manager 字典
            l = manager.list()  # manager 列表
            p_list = []         # 空的列表，为之后的添加进程实例
            for i in range(10):  # 启动多个子进程
                p = Process(target=run, args=(d,l))  # 起一子进程，执行run参数d，l
                p.start()
                p_list.append(p)  # 添加进程实例至列表
            for r in p_list:    # 循环子进程
                r.join()          # 等待子进程结束
            print(d)            # 打印最终的字典
            print(l)            # 打印最终的列表