# -*- coding = utf-8 -*-
# @Time : 2022/4/22 12:10 下午
# @Author : WyntonAB
# @File : 抓取一个视频_简单版.py
# @Software : PyCharm

# 想要抓取一个视频：
# 1、找到m3u8（各种手段）
# 2、通过m3u8下载到ts文件
# 3、通过各种手段（不仅是编码手段）把ts文件合并为一个mp3

'''
流程：
    1、拿到页面源代码
    2、从页面源代码中提取到m3u8的url
    3、下载m3u8
    4、读取m3u8文件，下载视频
    5、合并视频
'''

import requests

# 下载m3u8
# url = 'https://vod1.bdzybf7.com/20220414/Eec7vVjH/2000kb/hls/index.m3u8'
# resp = requests.get(url, headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
#     "Host": "vod1.bdzybf7.com"
# })
# with open('video/我们这一天第六季 第六集', mode='wb', encoding='utf-8') as f:
#     f.write(resp.content)
#
# resp.close()
# print("m3u8 download done!")


# 解析m3u8文件
n = 1
with open('index.m3u8', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()     # 去掉空行、空白、换行符
        if line.startswith('#'):    # 如果#开头我不要
            continue
        ts_url = "https://vod1.bdzybf7.com" + line

        # 下载视频的片段
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        resp2 = requests.get(ts_url, headers=headers)
        f = open(f'video/{n}.ts', mode='wb')
        f.write(resp2.content)
        f.close()
        resp2.close()
        print(f"{n} done!")
        n += 1


