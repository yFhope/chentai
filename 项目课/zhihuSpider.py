import requests

zhihu_url = "https://www.zhihu.com/hot"
headers = {
    'Cookie':'',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
response = requests.get(zhihu_url, headers=headers)
print(response.status_code)
print(response.text)