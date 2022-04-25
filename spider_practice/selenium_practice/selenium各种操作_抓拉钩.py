# -*- coding = utf-8 -*-
# @Time : 2022/4/25 9:59 上午
# @Author : WyntonAB
# @File : selenium各种操作_抓拉钩.py
# @Software : PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
# web.get('http://lagou.com')
#
# # 找到某个元素，点击它
# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[2]/a')
# el.click()  # 点击事件
#
# time.sleep(1)   # 让浏览器缓一缓
# # 找到输入框，输入python => 输入回车/点击搜索按钮
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
# time.sleep(1)
# # 选择工作地点为上海
# web.find_element_by_xpath('//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[3]').click()
#
# time.sleep(1)
# 查找数据存放的位置，进行数据提取
# 找到页面中存放数据的所有的div
# div_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
# for div in div_list:
#     job_name = div.find_element_by_xpath('./div[1]/div[1]/div[1]/a').text
#     job_price = div.find_element_by_xpath('./div[1]/div[1]/div[2]/span').text
#     job_company = div.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
#     print(job_name, job_price, job_company)
#
# web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
#
# # 如何进入新窗口中进行提取
# # 注意：在selenium眼中，新窗口是默认不切换过来的
# web.switch_to.window(web.window_handles[-1])
#
# # 在新窗口中提取内容
# job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
# print(job_detail)
#
# # 关掉子窗口
# web.close()
# # 变更selenium窗口视角，回到原来的窗口中
# web.switch_to.window(web.window_handles[0])
# print(web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text)


# 如果页面中遇到了iframe如何处理
web.get('https://www.91kanju.com/vod-play/541-2-1.html')
# 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，再然后才可以拿数据
time.sleep(1)
iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
web.switch_to.frame(iframe)     # 切换到iframe
tx = web.find_element_by_xpath("/html/head/title").text
print(tx)
# web.switch_to.default_content()     # 切换回原页面
