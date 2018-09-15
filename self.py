import requests
r=requests.get('https://www.bilibili.com/')
print(r.status_code)
print(r.content)
# print(r.text)

r=requests.get('https://www.bilibili.com/video/av31532423/?spm_id_from=333.334.ranking_douga.2')
print(r.url)
# print(r.text)
print(r.encoding)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())