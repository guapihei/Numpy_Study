#-*- codeing = utf-8 -*-

import urllib.request

# 对获取到的网页源码进行解码
# xy = urllib.request.urlopen("http://www.baidu.com")
# print(xy.read().decode('utf8'))

# post请求,需要传递个参数进去，模拟用户真实登录
# import urllib.parse
# data1 = bytes(urllib.parse.urlencode({"gua":"pi"}), "utf-8")
# xy = urllib.request.urlopen("https://httpbin.org/post",data = data1)
# print(xy.read().decode('utf8'))

# 异常检测,超时处理
# try:
#     xy = urllib.request.urlopen("https://httpbin.org/get",timeout = 0.01)
#     print(xy.read().decode('utf8'))
# except urllib.error.URLError as e:
#     print("time out")

# xy = urllib.request.urlopen("https://httpbin.org/get",timeout = 10)
# print(xy.status)
# print(xy.getheaders())
# print(xy.getheader("Date"))

# 伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
url = "http://www.douban.com"
data1 = bytes(urllib.parse.urlencode({"gua":"pi"}), "utf-8")
qq = urllib.request.Request(url = url,data = data1 ,headers = headers ,method = "POST")
xy = urllib.request.urlopen(qq,timeout = 10)
print(xy.status)
