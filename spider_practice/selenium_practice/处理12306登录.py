# -*- coding = utf-8 -*-
# @Time : 2022/4/25 9:16 下午
# @Author : WyntonAB
# @File : 处理12306登录.py
# @Software : PyCharm

from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('wynton', '1q2w3e4r.', '932509')

# 如果你的程序被识别到了怎么办？
# 1. 如果你的Chrome版本号小于88  在你启动浏览器的时候（此时没有加载任何网页内容），向页面嵌入js代码，去掉webdriver

# 2. 如果你的Chrome版本号大于等于88
option = Options()
# option.add_experimental_option(['excludeSwitches'], ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
web.find_element_by_xpath('//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
time.sleep(3)


# 先处理验证码
# 当存在图片选择验证时
try:
    verify_img_element = web.find_element_by_xpath('//*[@id="J-loginImg"]')

    # 用超级鹰去识别验证码
    dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
    result = dic['pic_str']  # x1,y1|x2,y2
    rs_list = result.split("|")
    for rs in rs_list:
        p_temp = rs.split(",")
        x = int(p_temp[0])
        y = int(p_temp[1])
        # 要让鼠标移动到某个位置，然后点击
        ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform()
    # 检查验证码是否正确
    time.sleep(10)
except:
    pass

# 输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('123456')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('123456')

# 点击登录
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)

# 拖拽滑块
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
