import time
import schedule
import requests
import pymysql
from lxml import etree
from jsonpath import jsonpath

zhihu_url = "https://www.zhihu.com/hot"
weibo_url = 'https://weibo.com/ajax/side/hotSearch'
bb_url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all&web_location=333.934&w_rid=d9dd79815e19908e5eeaba28dd58623d&wts=1712057009'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

url_list = [weibo_url, bb_url,zhihu_url]

def get_data(url,headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    raise Exception(f'error status_code: {response.status_code}')

def parse_zhihu(response):
    doc = etree.HTML(response.text)
    titles = doc.xpath('//h2[@class="HotItem-title"]/text()')
    urls = doc.xpath('//div[@class="HotItem-content"]/a/@href')
    for title,url in zip(titles, urls):
        save_data(title, url, 1)

def parse_weibo(response):
    word_schemes = jsonpath(response.json(),'$..word_scheme')
    word_urls = jsonpath(response.json(),'$..realtime..word')
    for title, word in zip(word_schemes, word_urls):
        url = f'https://s.weibo.com/weibo?q=%23{word}%23'
        save_data(title, url, 2)

def parse_bb(response):
    titles = jsonpath(response.json(), '$..title')
    urls = jsonpath(response.json(), '$..short_link_v2')
    for title, url in zip(titles, urls):
        save_data(title, url, 3)

def save_data(title,url,source):
    print(title, url, source)
    conn = pymysql.Connect(host='127.0.0.1',user='root',password='KaiFa@00#99',database='test')
    sql = "insert into hots_hotsmodel(title,url,source) values (%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,(title,url,source))
    conn.commit()
    conn.close()

def del_data():
    conn = pymysql.Connect(host='127.0.0.1', user='root', password='KaiFa@00#99', database='test')
    sql = "delete from hots_hotsmodel"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def task():
    for url in url_list:
        try:
            if 'zhihu' in url:
                headers['Cookie'] = "_ dF9Savu0hHlTQ=|906193|4:z_c0|80:MS4xVzFId0F3QUFBQUFtQUFBQVlBSlZUUnJRNTJhY2czX3BkRElESEJzLTJZdWJ6MkR4ckJ1TC1nPT0=|d04ebf479c02ac207557bbd5f15aa854b577f48d719c54d060186c56f65c95e4; _xsrf=32ba7e1f-e149-4998-be82-c6d9e92c6123; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1711589123,1711937814,1711969545,1712055944; tst=h; SESSIONID=PMbpRjU0xL1TxIdmp8KtWj9z1dCCViJHhbXQqkmSU9m; JOID=W1sdAEldpNb3UDy4RlblQbg5LW5QB-K_hglc5n0u4uyoKX7WIEpM15tRPbhM0td5LEHR8R2e4rQCjXRU9lgSw2I=; osd=Vl8XBUlQoNzyUDG8TFPlTLwzKG5dA-i6hgRY7Hgu7-iiLH7bJEBJ15ZVN71M39NzKUHc9Reb4rkGh3FU-1wYxmI=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1712061440; KLBRSID=ca494ee5d16b14b649673c122ff27291|1712063246|1712055943"
                response = get_data(url, headers)
                parse_zhihu(response)
            elif 'weibo' in url:
                response = get_data(url, headers)
                parse_weibo(response)
            else:
                response = get_data(url, headers)
                parse_bb(response)
        except Exception as e:
            print(e,url)
            continue
    print('---' * 35)


if __name__ == '__main__':
    while True:
        del_data()
        task()
        time.sleep(10)

