import requests
from jsonpath import jsonpath

url = 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={}&web_location=333.934&w_rid=05d7dc9dea7164c3943def5ef14d014b&wts=1711021892'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}

def get_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    raise Exception('数据请求失败~')

def parse_data(data):
    data = data.json()
    up_names = jsonpath(data,'$..name')
    titles = jsonpath(data,'$..title')
    views = jsonpath(data,'$..view')
    danmakus = jsonpath(data,'$..danmaku')
    bvids = jsonpath(data,'$..bvid')
    for name,tit,view,danmu,vid in zip(up_names,titles,views,danmakus,bvids):
        print(tit)
        print(name)
        print(view)
        print(danmu)
        print(vid)
        print('---'*30)

if __name__ == '__main__':
    for i in range(1,11):
        print(f'正在抓取第{i}页')
        data = get_data(url.format(i))
        parse_data(data)