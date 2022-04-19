# -*- coding = utf-8 -*-
# @Time : 2022/4/18 7:51 下午
# @Author : WyntonAB
# @File : re.py
# @Software : PyCharm

import re
# findall:匹配字符串中所有符合正则的内容
list = re.findall(r"\d+","我的电话号码是：10010，我女朋友的电话号码是：10086")
print(list)

# finditer:匹配字符串中的所有内容，返回的是迭代器，从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+","我的电话号码是：10010，我女朋友的电话号码是：10086")
print(it)
for i in it:
    print(i)
    print(i.group())

# search:找到一个结果就返回，返回的是match对象，拿数据需要.group()
s = re.search(r"\d+","我的电话号码是：10010，我女朋友的电话号码是：10086")
print(s.group())

# match:从头开始匹配，拿数据需要.group()
m = re.search(r"\d+","10010，我女朋友的电话号码是：10086")
print(m.group())

# 预加载正则表达式
obj = re.compile(r"\d+")
rep = obj.findall("我的电话号码是：10010，我女朋友的电话号码是：10086")
print(rep)

# re.S让.能匹配换行符
# (P?<分组name>正则表达式)可以单独从正则匹配的内容中进一步提取内容
