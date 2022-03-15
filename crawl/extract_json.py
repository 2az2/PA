import requests
import json
import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
res = requests.get(url,headers=headers,timeout=5)
html = res.content
data = json.loads(html)
'''
with open("js.txt","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii = False,indent = 4)
'''
# with open("js.txt","r",encoding="utf-8") as f:
#     data=json.load(f)
cities = jsonpath.jsonpath(data,'$..name')
print(cities)
