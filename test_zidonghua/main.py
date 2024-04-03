import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # 封装了一些查找器
from selenium.webdriver.common.keys import Keys  # 封装了一些功能按钮
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
'''
1、打开百度
2、在搜索框输入Python
3、点击搜索按钮
'''
browser = webdriver.Chrome()  # browser 驱动对象
# try:
# 1 打开百度
browser.get('https://www.baidu.com')  # 调用浏览器驱动对象访问站点
# 2 输入 Python 文本
# ？ 我怎么知道输入框在哪？
text_input = browser.find_element(By.ID,'kw')  # 拿到了输入框
# 向输入框中输入内容
text_input.send_keys('美女')
# 点击搜索按钮
browser.find_element(By.ID,'su').click()

# 按回车按钮
# text_input.send_keys(Keys.ENTER)

# 等待事件  -- 怕网速慢
# wait = WebDriverWait(browser, 10)  # 参数1：浏览器对象  参数2：时间 秒
# wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#
# print(browser.current_url)  # 看url
# print(browser.get_cookies())  # 看cookie
# print(browser.page_source)  # 看源代码
time.sleep(10)
#
# finally:
#     #     print("23333")
#     browser.close()  # 关闭浏览器