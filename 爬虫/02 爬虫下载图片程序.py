'''

抓图片 保存到本地
'''


# f = open('qwe.txt','a')
# f.write('34567890')
# f.close()
import requests
img_url = "	https://www.baidu.com/img/flexible/logo/pc/result@2.png"


response = requests.get(img_url)
print(response.status_code)
print(response.content)

f = open('kldjfdjskl.png','wb')
f.write(response.content)
f.close()
