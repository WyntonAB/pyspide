# -*- coding = utf-8 -*-
# @Time : 2022/4/19 11:14 上午
# @Author : wuwentao
# @File : 新发地菜价.py
# @Software : PyCharm

import requests
import csv

url = "http://www.xinfadi.com.cn/getPriceData.html"

f = open("新发地菜价_data.csv",mode="w")
csvwriter = csv.writer(f)
print("开始爬取！")
for i in range(1,14869):
    data = {
        "limit": 20,
        "current": i,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": "",
    }
    resp = requests.post(url,data=data)
    resp_list = resp.json()['list']
    # print(resp_list)
    for j in range(0,20):
        data_list=[]
        name = resp_list[j]['prodName']
        cat = resp_list[j]['prodCat']
        lowprice = resp_list[j]['lowPrice']
        avgprice = resp_list[j]['highPrice']
        highprice = resp_list[j]['avgPrice']
        place = resp_list[j]['place']
        spec = resp_list[j]['specInfo']
        unit = resp_list[j]['unitInfo']
        pubdata = resp_list[j]['pubDate']
        data_list.append(name)
        data_list.append(cat)
        data_list.append(lowprice)
        data_list.append(avgprice)
        data_list.append(highprice)
        data_list.append(place)
        data_list.append(spec)
        data_list.append(unit)
        data_list.append(pubdata)
        csvwriter.writerow(data_list)
    print(f"已爬取第{i}页")
print("over!")
f.close()