# -*- coding = utf-8 -*-
# @Time : 2022/4/25 7:31 下午
# @Author : WyntonAB
# @File : 无头浏览器_艺恩数据库.py
# @Software : PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

# 准备好参数配置:无头浏览器
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-cpu")


web = Chrome(options=opt)       # 把参数配置设置到浏览器中
# web.get("https://endata.com.cn/BoxOffice/BO/Year/index.html")     # 老链接
web.get("https://ys.endata.cn/BoxOffice/Movie")


'''>>>老链接内容提取方法<<<'''
# # 定位到下拉框
# sel_el = web.find_element_by_xpath('//*[@id="OptionData"]')
# # 对元素进行打包，包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器调整选项
# for i in range(len(sel.options)):   # i就是每个下拉选项索引的位置
#     sel.select_by_index(i)  # 按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"].table')
#     print(table.text)
#     print("="*100)
#
# print("程序运行完毕！")
# web.close()


# 如何拿到页面代码Elements（经过数据加载以及js执行之后的结果html内容）
print(web.page_source)

web.close()