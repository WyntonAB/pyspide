# -*- coding = utf-8 -*-
# @Time : 2022/4/20 7:50 下午
# @Author : WyntonAB
# @File : 代理.py
# @Software : PyCharm

import requests
# 118.190.244.234:3128
proxies = {
    "https": "https://118.190.244.234:3128",
    # "http":""
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)