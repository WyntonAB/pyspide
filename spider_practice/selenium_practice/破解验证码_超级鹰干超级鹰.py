# -*- coding = utf-8 -*-
# @Time : 2022/4/25 8:19 下午
# @Author : WyntonAB
# @File : 破解验证码_超级鹰干超级鹰.py
# @Software : PyCharm

# 1. 图像识别
# 2. 寻找互联网上成熟的验证码破解工具

from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()
web.get("https://www.chaojiying.com/user/login/")

# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('username', 'password', '932509')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 向页面中填入用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('wynton')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('1q2w3e4r.')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(5)

# 点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()