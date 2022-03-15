import requests
from functools import wraps
url="http://httpbin.org/get"
baidu="http://www.baidu.com"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
# get 参数为 params
params={
    "Bella":"Bellaris"
}
# 高匿代理为 proxies
# 可自定义代理服务器
proxies = {
  "http":"http://IP地址:端口号",
  "https":"https://IP地址:端口号"
}
# post 参数为 data
data={
    "Bella":"Bellaris"
}

# res=requests.get(url,headers=headers,verify=False) # 不验证CA证书
# res=requests.get(url,headers=headers,params=params)
# res=requests.post(url,headers=headers,data=data)

url="http://192.168.168.168"
res=requests.post(url,headers=headers,data=data)

text=res.text
content=res.content
code=res.status_code
req_head=res.request.headers
head=res.headers
cookie=res.cookies
# with open("hm.txt","w",encoding="utf-8") as f:
#     f.write(content.decode("utf-8"))
# print(text)
# print(content)
print(content.decode("utf-8"))
# print(code)
# print(req_head)
# print(head)
# print(cookie)

'''
# save png
url="https://i0.hdslb.com/bfs/article/55e156e86d6187bb635909d636ce2ddd42814d2b.jpg@942w_1281h_progressive.webp"
res=requests.get(url,timeout=2)
with open('Bella2.jpg','wb') as f:
    f.write(res.content)
'''
