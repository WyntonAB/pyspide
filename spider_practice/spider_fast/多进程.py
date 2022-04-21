# -*- coding = utf-8 -*-
# @Time : 2022/4/21 3:49 下午
# @Author : WyntonAB
# @File : 多进程.py
# @Software : PyCharm

from multiprocessing import Process

def func():
    for i in range(1000):
        print("子进程", i)

if __name__ == '__main__':
    p = Process(target=func)
    p.start()

    for i in range(1000):
        print("主进程", i)