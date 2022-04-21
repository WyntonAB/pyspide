# -*- coding = utf-8 -*-
# @Time : 2022/4/21 3:20 下午
# @Author : WyntonAB
# @File : 多线程.py
# @Software : PyCharm

from threading import Thread

# part one
def fanc(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    t1 = Thread(target=fanc, args=("子线程1",))     # 创建线程，并给线程安排认为    # 传递参数必须是元组
    t1.start()   # 多线程工作状态为可以开始工作状态，具体执行时间由CPU决定

    t2 = Thread(target=fanc, args=("子线程2",))
    t2.start()

    for i in range(1000):
        print("main", i)

# part two
# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程", i)
#
# if __name__ == '__main__':
#     t = MyThread()
#     # t.run()    # 这是一种方法的调用 -> 单线程
#     t.start()   # 开始线程
#     for i in range(1000):
#         print("主线程", i)
