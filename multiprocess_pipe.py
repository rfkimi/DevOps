#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import  Process,Pipe


def f(conn):
    conn.send("from child1")  # 发送数据
    conn.send("from child2")  # 发送数据
    print('client recv:',conn.recv())  # 接收数据
    conn.close()


if __name__ == '__main__':
    a_conn, b_conn = Pipe()
    p = Process(target=f, args=(b_conn, ))
    p.start()
    print(a_conn.recv())
    print(a_conn.recv())
    a_conn.send('from parent')  # 父进程发送数据
    p.join()
