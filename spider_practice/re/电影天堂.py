# -*- coding = utf-8 -*-
# @Time : 2022/4/17 9:45 下午
# @Author : wuwentao
# @File : 电影天堂.py
# @Software : PyCharm
import requests
import re
import csv

domain = "https://dytt89.com/"
resp = requests.get(domain,verify=True)     # verify=False去掉安全验证
resp.encoding = "gb2312"    # 指定字符集
# print(resp.text)

# 拿到ul里面的li
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<movie_name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">',re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group("ul")
    # print(ul)

# 在html中a标签<a href=url>titel</a>

    # 提取子页面内容
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面的URL地址：域名+子页面地址
        child_href = domain + itt.group('href').strip('/')
        child_href_list.append(child_href)
f = open("电影天堂2022必看电影_data.csv", mode="w")
csvwriter = csv.writer(f)
# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    # print(result3.group('movie_name'))
    # print(result3.group('download'))
    dic = result3.groupdict()
    csvwriter.writerow(dic.values())

print("over!")
f.close()
