# -*- coding = utf-8 -*-
# @Time : 2022/4/20 5:05 下午
# @Author : WyntonAB
# @File : 模拟用户登录_处理cookie_17小说网.py
# @Software : PyCharm

# 登录 -> 得到cookie
# 带着cookie去请求到书架的URL -> 书架上的内容

# 我们可以使用session进行请求 -> session可以认为是一连串的请求，并且在这个请求过程中cookie不会丢失

import requests

# 会话
session = requests.session()

baseurl = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "15819223721",
    "password": "123321qwe"
}
session.post(baseurl, data=data)
# print(resp.text)
# print(resp.cookie)

shelfurl = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"

resp = session.get(shelfurl)

for it in resp.json()['data']:
    print(it['bookName'])