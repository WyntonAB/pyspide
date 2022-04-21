# -*- coding = utf-8 -*-
# @Time : 2022/4/21 3:58 下午
# @Author : WyntonAB
# @File : 进程池和线程池入门.py
# @Software : PyCharm

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")

    # 等待线程池中的任务全部执行完毕，才继续执行（守护）
    print("123")