# -*- coding = utf-8 -*-
# @Time : 2022/4/17 9:20 下午
# @Author : WyntonAB
# @File : 豆瓣喜剧电影.py
# @Software : PyCharm
import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

response = requests.get(url=url,params=param,headers=headers)

print(response.json())
response.close()
