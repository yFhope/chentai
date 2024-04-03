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
browser.get('https://careers.tencent.com/jobopportunity.html')  # 调用浏览器驱动对象访问站点
# 2 输入 Python 文本
# ？ 我怎么知道输入框在哪？
text_input = browser.find_element(By.ID,'q')  # 拿到了输入框
text_input = browser.find_element(By.ID,'q')  # 拿到了输入框
# 向输入框中输入内容
# text_input.send_keys('手机')
# 按回车按钮
# text_input.send_keys(Keys.ENTER)
time.sleep(1.2)
print(browser.page_source)
time.sleep(1000)
