import requests
url = "https://www.duitang.com/search/?kw=校花&type=feed"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}
response = requests.get(url, headers=headers)
# 获取网页源代码
html_data = response.text
# 1、安装 导包  pip install lxml
from lxml import etree
# 2、把html文档转换成XML  etree.HTML()
xml_doc = etree.HTML(html_data)
print(xml_doc)
# 3、通过xml文档对象的属性 来解析数据
names = xml_doc.xpath('//a[@class="p"]/text()')
print(names)



