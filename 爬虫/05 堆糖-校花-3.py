'''

https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&after_id=48&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1710938779879
'''

import requests
from jsonpath import jsonpath
url = 'https://www.duitang.com/napi/blogv2/list/by_search/?kw=校花&after_id=0&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1710938779879'
headers_a = {
    # "aaa":"dasdsadsad",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}
res = requests.get(url,headers=headers_a)
dict_datas = res.json()

# img_list = dict_datas['data']['object_list']['photo']['path']
# # print(da_list)
# for img_obj in img_list:
#     img_url = img_obj['photo']['path']
#     print(img_url)

usernames = jsonpath(dict_datas,'$..username')
imgurls = jsonpath(dict_datas,'$..path')

for uname in usernames:
    print(uname)

# pip install jsonpath -i https://pypi.tuna.tsinghua.edu.cn/simple
