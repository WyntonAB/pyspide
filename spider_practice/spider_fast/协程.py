# -*- coding = utf-8 -*-
# @Time : 2022/4/21 5:12 下午
# @Author : WyntonAB
# @File : 协程.py
# @Software : PyCharm

import time
import asyncio

'''
async def fuc():
    print(1)
    time.sleep(3)   # 让线程处于阻塞状态，cpu不为我工作
    print(2)

if __name__ == '__main__':
    g = fuc()   # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
    # print(g)
    asyncio.run(g)  # 协程程序的运行需要asyncio模块的支持

# input() requests.get() 程序也是处于阻塞状态
'''

#
# async def fuc1():
#     print(1)
#     # time.sleep(3)   # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)    # 异步操作的代码 await表示当程序进入睡眠时，将程序挂起
#     print(2)
#
# async def fuc2():
#     print(3)
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print(4)
#
# async def fuc3():
#     print(5)
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print(6)
#
# if __name__ == '__main__':
#     t1 = fuc1()
#     t2 = fuc2()
#     t3 = fuc3()
#     tasks = [
#         t1, t2, t3
#     ]
#     t1 = time.time()
#     # 一次性启动多个任务（协程）
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2 - t1)



async def fuc1():
    print(1)
    await asyncio.sleep(3)
    print(2)

async def fuc2():
    print(3)
    await asyncio.sleep(2)
    print(4)

async def fuc3():
    print(5)
    await asyncio.sleep(4)
    print(6)

async def main():
    # 第一种写法
    # f1 = fuc1()
    # await f1    # 一般await操作放在协程对象前面

    # 第二种写法（推荐）
    tasks = {
        asyncio.create_task(fuc1()),
        asyncio.create_task(fuc2()),
        asyncio.create_task(fuc3())
    }
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # 一次性启动多个任务（协程）
    asyncio.run(main())