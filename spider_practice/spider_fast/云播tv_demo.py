# -*- coding = utf-8 -*-
# @Time : 2022/4/22 5:16 下午
# @Author : WyntonAB
# @File : demo.py
# @Software : PyCharm

import requests
import re

url1 = "https://www.yunbtv.net/vodplay/yueyudiyiji-1-1.html"
obj1 = re.compile('"vod_class".*?"url":"(?P<url2>.*?)","url_next"')
obj2 = re.compile('<title>(?P<title>.*?)</title>')

resp1 = requests.get(url1)
# print(resp1.text)
result1 = obj1.search(resp1.text)
result2 = obj2.search(resp1.text)
url2 = result1.group('url2').replace('\\', '')
title = result2.group('title').rsplit('-')[0]


resp2 = requests.get(url2)
f = open(f"越狱第一季/base_{title}.m3u8", mode='wb')
f.write(resp2.content)
f.close()
resp2.close()

with open(f"越狱第一季/base_{title}.m3u8", mode='r', encoding='utf-8') as f:     #f"越狱第一季/base_{title}.m3u8"
    for base_line in f:
        base_line = base_line.strip()
        if base_line.startswith('#'):
            continue
        url3 = "https://v4.monidai.com/" + base_line

resp3 = requests.get(url3)
f = open(f"越狱第一季/{title}.m3u8", mode='wb')
f.write(resp3.content)
f.close()
resp3.close()

n = 1
with open(f'越狱第一季/{title}.m3u8', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        ts_url = "https://v4.monidai.com" + line
        resp4 = requests.get(ts_url)
        f = open(f'越狱第一季/{n}.ts', mode='wb')
        f.write(resp4.content)
        f.close()
        resp4.close()
        print(f"{n} done!")
        n += 1


