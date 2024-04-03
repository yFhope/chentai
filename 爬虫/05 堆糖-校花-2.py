import requests
from lxml import etree

url_a = "https://www.duitang.com/search/?kw=校花&type=feed"
headers_a = {
    # "aaa":"dasdsadsad",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}


# 1、2 请求数据与获取响应
def get_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    raise Exception("状态码非200，请求失败")


# 3、解析数据
def parse_data(response):
    xml_doc = etree.HTML(response.text)
    names = xml_doc.xpath('//a[@class="p"]/text()')
    hrefs = xml_doc.xpath('//a[@class="a"]/img/@src')
    for name, src in zip(names, hrefs):
        print(name, src)
        response = get_data(src,headers_a)
        save_imgs(response.content,name)

# 4、保存数据
def save_imgs(img_content, name):
    f = open('imgs/' + name + '.jpg', 'wb')
    f.write(img_content)
    f.close()


if __name__ == '__main__':
    html_data = get_data(url_a, headers_a)
    parse_data(html_data)
