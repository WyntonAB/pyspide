# -*- coding = utf-8 -*-
# @Time : 2022/4/20 5:40 下午
# @Author : WyntonAB
# @File : 防盗链处理_梨视频.py
# @Software : PyCharm

import requests
import re
import time

url = "https://www.pearvideo.com/"
obj = re.compile(r'<a href="video_(?P<href>.*?)".*?'
                 r'<div class="vervideo-title">(?P<title>.*?)</div>',re.S)

resp = requests.get(url)
# print(resp.text)

# 获取梨视频首页的视频ID
result = obj.finditer(resp.text)

i = 0
for it in result:
    contId = it.group('href')
    title = it.group('title')

    # 拉视频的网址
    href = url + 'video_' + contId
    # print(href)

    videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8805350066520099"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
        # 防盗链：溯源，本次请求的上一级是谁
        "Referer": href
    }
    video_resp = requests.get(videoStatusUrl, headers=headers)
    dic = video_resp.json()
    srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
    systemTime = dic["systemTime"]

    # 获取到的链接：https://video.pearvideo.com/mp4/adshort/20220420/1650452824229-15864631_adpkg-ad_hd.mp4
    # 真实链接：https://video.pearvideo.com/mp4/adshort/20220418/cont-1759035-15863820_adpkg-ad_hd.mp4

    srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
    # 下载视频
    with open(f"pearvideo/{title}.mp4", mode="wb") as f:
        f.write(requests.get(srcUrl).content)
    i += 1
    print(f"已爬取{i}个视频")
    time.sleep(1)

print("over!")

