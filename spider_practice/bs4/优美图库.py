# -*- coding = utf-8 -*-
# @Time : 2022/4/19 7:48 下午
# @Author : WyntonAB
# @File : 优美图库.py
# @Software : PyCharm

# 1.拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址   img -> src
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.youmeitu.com/weimeitupian/"

resp = requests.get(url)
resp.encoding = 'utf-8'

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a", class_="TypeBigPics")

for a in alist:
    href = url + a.get('href').strip("/")   # Beautifulsoup中拿属性的值用.get

    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text

    child_page = BeautifulSoup(child_page_text, "html.parser")
    img = child_page.find("p", align="center").find("img")
    src = "https://www.youmeitu.com/" + img.get('src').strip('/')

    img_resp = requests.get(src)
    # img_resp.content    # 这里拿到的是字节
    img_name = src.split("/")[-1]   # 拿到url最后一个/以后的内容
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)   # 图片内容写入文件

    print("over!!!", img_name)
    time.sleep(1)
    # break

print("all over!!!")
