# -*- coding = utf-8 -*-
# @Time : 2022/4/18 8:14 下午
# @Author : wuwentao
# @File : 豆瓣电影Top250.py
# @Software : PyCharm
import requests
import re
import csv

baseurl = f"https://movie.douban.com/top250?start="
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}
f = open("豆瓣Top250_data.csv",mode="w")
csvwriter = csv.writer(f)
print("开始爬取网页...")
for page in range(0,10):
    url = baseurl + str(page*25)
    response = requests.get(url,headers=headers)
    page_content = response.text
    response.close()
    print(f"开始爬取第{page+1}页数据")
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                     r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'<span>(?P<num>.*?>)人评价</span>',re.S)
    result = obj.finditer(page_content)
    for it in result:
        dic = it.groupdict()
        dic["year"]=dic["year"].strip()
        csvwriter.writerow(dic.values())
    print(f"已爬取{page*25+25}条数据")
print("over!")
f.close()
