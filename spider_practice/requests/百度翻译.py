# -*- coding = utf-8 -*-
# @Time : 2022/4/17 9:02 下午
# @Author : wuwentao
# @File : 百度翻译.py
# @Software : PyCharm
import requests
name = input("请输入要翻译的单词：")
url = "https://fanyi.baidu.com/sug"
data = {
    "kw":name
}
response = requests.post(url,data=data)
print(response.json())