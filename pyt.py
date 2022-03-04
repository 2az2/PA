import urllib.request
import urllib.parse


#urllib.request.urlopen('http://www.baidu.com')
#print(type(response))


# response=urllib.request.urlopen('http://www.bilibili.com',timeout=1)
# print(response.status)


# try:
#     response=urllib.request.urlopen('http://www.baidu.com',timeout=1)
#     # print(response.read().decode('utf-8'))
#     # print(response.getheaders())
#     # print(response.getheader("Bdqid"))
# except TimeoutError:
#     print("Time Out")


# url="http://httpbin.org/post"
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'Leo'}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url="http://www.bilibili.com"
# response=urllib.request.urlopen(url,timeout=1)
# print(response.read().decode('utf-8'))
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
req=urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))