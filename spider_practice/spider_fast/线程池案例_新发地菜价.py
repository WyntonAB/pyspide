# -*- coding = utf-8 -*-
# @Time : 2022/4/21 4:07 下午
# @Author : WyntonAB
# @File : 线程池案例_新发地菜价.py
# @Software : PyCharm

import requests
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("新发地菜价_data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

# 下载一页的数据
def download_one_page(data, i):
    resp = requests.post("http://www.xinfadi.com.cn/getPriceData.html", data=data)
    resp_list = resp.json()['list']
    for it in resp_list:
        data_list = []
        its = list(it.values())
        data_list.append(its[1])
        data_list.append(its[3])
        data_list.append(its[6])
        data_list.append(its[7])
        data_list.append(its[8])
        data_list.append(its[9])
        data_list.append(its[10])
        data_list.append(its[12])
        csvwriter.writerow(data_list)
    print(f"第{i}页爬取完毕！")

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1,14869):
            data = {
                "limit": 20,
                "current": {i},
                "pubDateStartTime": "",
                "pubDateEndTime": "",
                "prodPcatid": "",
                "prodCatid": "",
                "prodName": "",
            }
            # 将任务提交给线程池
            t.submit(download_one_page, data, i)
    print("全部下载完成！")
