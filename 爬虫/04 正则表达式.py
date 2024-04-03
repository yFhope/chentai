import requests
url = "https://book.douban.com/latest?icn=index-latestbook-all"

head = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}
res = requests.get(url,headers=head)

print(res.status_code)
# print(res.text)


import re

bsd = '<a.class="fleft".*?>(.*?)</a>'
book_name = re.findall(bsd,res.text)
print(book_name)

bsd = '<a.class="fleft".*?href="(.*?)">'
book_url = re.findall(bsd,res.text)
print(book_url)

