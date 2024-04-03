import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
# browser.switch_to.frame('iframeResult')

# A = browser.find_element(By.CSS_SELECTOR,'#draggable')
# B = browser.find_element(By.CSS_SELECTOR,'#droppable')

# actions = ActionChains(browser)  # 产生一个动作执行器
# actions.drag_and_drop(A, B) #  A移动到B
# actions.perform()  # 执行动作链
browser.execute_script('alert("666666666")')
time.sleep(15)