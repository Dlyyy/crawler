import re
import requests

respose=requests.get('http://www.xiaohuar.com/v/')
print(respose.status_code)# 响应的状态码
print(respose.content)  #返回字节信息,无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
print(respose.text)  #返回文本内容
urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
url=urls[8]
result=requests.get(url)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
print(mp4_url)

video=requests.get(mp4_url)

with open('E:/PythonProject01/download/1.mp4','wb') as f:
    f.write(video.content)