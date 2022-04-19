# -*- coding = utf-8 -*-
# @Time : 2022/4/19 9:30 下午
# @Author : wuwentao
# @File : 猪八戒网.py
# @Software : PyCharm

# 拿页面源代码
# 提取和解析数据

import requests
from lxml import etree
import csv

search = input("请输入想要搜索的内容：")
url = f"https://shanghai.zbj.com/search/f/?kw=saas"

f = open(f"猪八戒网_{search}_data.csv",mode="w")
csvwriter = csv.writer(f)

resp = requests.get(url)
# 解析
html = etree.HTML(resp.text)
# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for div in divs:    # 每一个服务商的信息
    data_list = []
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = f"{search}".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip("\n")
    location = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    data_list.append(price)
    data_list.append(title)
    data_list.append(com_name)
    data_list.append(location)
    csvwriter.writerow(data_list)
f.close()
print("over!")

