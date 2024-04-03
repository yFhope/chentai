# pip install requests
'''
TODO 爬虫入门初体验
'''

import requests  # 导包
# 1、发起请求
# 2、获取响应
url = "https://www.mi.com/shop"
response = requests.get(url)  # 发起请求
print(response.status_code)  # 获取状态码
print(response.text)   # 获取网页源码



# 3、解析内容

# 4、保存数据
