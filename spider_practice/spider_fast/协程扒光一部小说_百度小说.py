# -*- coding = utf-8 -*-
# @Time : 2022/4/21 9:46 下午
# @Author : WyntonAB
# @File : 协程扒光一部小说_百度小说.py
# @Software : PyCharm

# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}  => 章节名称 cid
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1

import requests
import aiohttp
import aiofiles
import asyncio
import json

# 1、同步操作：访问getCatalog 拿到所有章节的名称和cid
# 2、异步操作：访问getChapterContent 下载所有文章的内容

# 1、同步操作：访问getCatalog 拿到所有章节的名称和cid
async def getCatalog(url):
    resp = requests.get(url)
    items = resp.json()['data']['novel']['items']
    tasks = []
    for item in items:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid, book_id, title, url)))
        # break

    await asyncio.wait(tasks)


# 2、异步操作：访问getChapterContent 下载所有文章的内容
async def aiodownload(cid, book_id, title, url):
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Referer": url      # 防盗链接处理
    }
    data = json.dumps(data)

    getChapterContent_url = "http://dushu.baidu.com/api/pc/getChapterContent?data=" + data
    async with aiohttp.ClientSession() as session:
        async with session.get(getChapterContent_url, headers=headers) as resp:
            dic = await resp.json()
            content = dic['data']['novel']['content']

            #写入文件
            async with aiofiles.open(f'novel/{title}.text', mode='w', encoding='utf-8') as f:
                await f.write(content)    # 把小说内容写入
                print(f"已爬取 >> {title}!")


if __name__ == '__main__':
    book_id = "4306063500"
    getCatalog_url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id +'"}'
    asyncio.run(getCatalog(getCatalog_url))
    print("已全部爬取！")


