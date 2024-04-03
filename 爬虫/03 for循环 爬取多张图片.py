img_list = [
    "https://www.baidu.com/img/flexible/logo/pc/result@2.png",
    "https://c-ssl.dtstatic.com/uploads/item/201511/17/20151117121559_3w8u4.thumb.1000_0.jpeg"
]

import requests

number = 1  # 自增变量 用于图片命名
for url in img_list:  # 循环 遍历图片列表  拿到每一个url给requests请求
    print(url)  # 获取到的每一个url链接
    res = requests.get(url)  # 请求并获取数据

    file_name = ''+str(number)+'.png'  # 构建文件名
    f = open(file_name,'wb')  # 写入 保存到文件
    f.write(res.content)
    f.close()
    number += 1  # 自增 +1