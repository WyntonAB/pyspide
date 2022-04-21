# -*- coding = utf-8 -*-
# @Time : 2022/4/21 9:10 下午
# @Author : WyntonAB
# @File : aiohttp模块_优美图库.py
# @Software : PyCharm

# requests.get()同步的代码 -> 异步操作aiohttp模块

import aiohttp
import asyncio

urls = {
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/3odogkd24oc.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/nzlhxqndoa4.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/q3f3dzgivbx.jpg"
}

async def aiodownload(url):

    # s = aiohttp.ClientSession() <=> requests
    # s.get()   .post   <=>   requests.get()   .post
    # 1、发送请求   2、得到图片内容    3、保存文件

    name = url.rsplit("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp.content.read()  <==>  resp.content()
            with open("img/" + name, mode="wb") as f:
                f.write(await resp.content.read())      # 异步操作读取文件时要加await

    print(name, "完成！")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())