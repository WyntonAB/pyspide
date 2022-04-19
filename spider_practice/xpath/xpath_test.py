# -*- coding = utf-8 -*-
# @Time : 2022/4/19 9:16 下午
# @Author : wuwentao
# @File : xpath.py
# @Software : PyCharm

from lxml import etree
tree = etree.XML()
result = tree.xpath("/")
# //表示后代
# /*/：*表示通配符
# xpath的顺序是从1开始数的
# [@xxx=xxx] 属性的筛选
# ./表示相对查找
# /@xxx 拿属性的值