# -*- coding = utf-8 -*-
# @Time : 2022/4/22 7:20 下午
# @Author : WyntonAB
# @File : 抓取一个视频_云播tv.py
# @Software : PyCharm

import requests
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
import os


def get_first_m3u8_url(url):
    obj1 = re.compile('"vod_class".*?"url":"(?P<m3u8_url>.*?)","url_next"')
    obj2 = re.compile('<title>(?P<title>.*?)</title>')

    resp = requests.get(url)
    result = resp.text
    m3u8_url = obj1.search(result).group('m3u8_url').replace("\\", "")
    title = obj2.search(result).group('title').rsplit("-")[0]
    m3u8_data = [m3u8_url, title]

    return m3u8_data
    # return ['https://v4.szjal.cn/20191003/emVicKUk/index.m3u8', "越狱第一季_第01集_在线播放"]  # 测试用


def download_m3u8_file(url, name):
    resp = requests.get(url)
    with open(name, mode='wb') as f:
        f.write(resp.content)


'''
def read_m3u8_file(file_path):
    m3u8_file_data = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            m3u8_file_data.append(line)

    return m3u8_file_data


def download_video_ts(url, ts_path):
    resp = requests.get(url)
    with open(ts_path, mode="wb") as f:
        f.write(resp.content)
    print("done!")
'''


async def download_ts(url, file_path, session):
    async with session.get(url) as resp:
        async with aiofiles.open(file_path, mode='wb') as f:
            await f.write(await resp.content.read())        # 把下载到的内容写入到文件中
    name = file_path.split('/')[-1]
    print(f"{name}下载完毕")


async def aio_download(up_url, file_path):
    tasks = []
    async with aiohttp.ClientSession() as session:      # 提前准备好session
        async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
            async for line in f:
                if line.strip().startswith('#'):
                    continue
                line = line.strip()    # 去掉没用的空行和换行
                # 拼接真正的ts路径
                ts_url = up_url + line
                ts_path = f"{file_path.split('/')[0]}/{line.split('/')[-1]}"
                task = asyncio.create_task(download_ts(ts_url, ts_path, session))       # 创建任务
                tasks.append(task)

            await asyncio.wait(tasks)       # 等待任务解释


def get_key(url):
    resp = requests.get(url)
    return resp.text


async def dec_ts(file_path, key):
    aes = AES.new(key=key, IV=b'0000000000000000', mode=AES.MODE_CBC)
    async with aiofiles.open(file_path, mode='rb') as f1,\
        aiofiles.open(f"{file_path}_temp", mode='rb') as f2:

        bs = await f1.read()    # 从源文件读取内容
        await f2.write(aes.decrypt(bs))     # 把解密后的内容写入文件
    namethod = name = file_path.split('/')[-1]
    print(f"{name}处理完毕")


async def aio_dec(key, file_path):
    tasks = []
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
        async for line in f:
            if line.startswith('#'):
                continue
            line = line.split()
            ts_path = f"{file_path.split('/')[0]}/{line.split('/')[-1]}"
            #开始创建异步任务
            task = asyncio.create_task(dec_ts(ts_path, key))
            tasks.append(task)
        await asyncio.wait(tasks)


def merge_ts(file_path):
    # mac: 1.ts 2.ts 3.ts > xxx.mp4
    lst = []
    path = file_path.split('/')[0]
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.strip().split('/')[-1]
            lst.append(f"{path}/{line}")        # 不需解密的ts
            # lst.append(f"{path}/{line}_temp")  # 需要解密的ts

    s = " ".join(lst)  # 1.ts 2.ts 3.ts
    os.system(f"cat {s} > {path}/movie.mp4")
    print("合并完成！")


def main(url):
    # 1、拿到主页面的源代码，找到第一层的m3u8的下载地址
    first_m3u8_data = get_first_m3u8_url(url)
    first_m3u8_url = first_m3u8_data[0]
    video_title = first_m3u8_data[1]

    print(f"开始爬取{video_title}！")

    # 2.1 下载第一层的m3u8文件
    download_m3u8_file(first_m3u8_url, f"{video_title}/{video_title}_first_m3u8.txt")
    # 2.2 下载第二层的m3u8文件
    with open(f"{video_title}/{video_title}_first_m3u8.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                line = line.strip()
                second_m3u8_url = "https://v4.monidai.com" + line
                download_m3u8_file(second_m3u8_url, f"{video_title}/{video_title}_second_m3u8.txt")
                print("m3u8 download done!")


    # 3、下载视频
    # 异步协程
    asyncio.run(aio_download("https://v4.monidai.com", f"{video_title}/{video_title}_second_m3u8.txt"))     # 测试的时候可以省略
    print("ts download all done!")

    """
    ------some m3u8 file need this part------
    4.1 拿到密钥
    key_url = 'https://v4.monidai.com' + 'key.key'
    key = get_key(url)
    4.2 解密
    asyncio.run(aio_dec(key))
    """

    # 5、合并ts文件为mp4文件
    merge_ts(f"{video_title}/{video_title}_second_m3u8.txt")


if __name__ == '__main__':
    print("begin!")
    url = "https://www.yunbtv.net/vodplay/yueyudiyiji-1-1.html"
    main(url)
    print("all finish!")
