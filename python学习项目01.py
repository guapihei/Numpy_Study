#-*- codeing = utf-8 -*-

from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，文字匹配
import urllib.request,urllib.error #制定URL
import openpyxl #进行excel操作
import sqlite3 #进行SQLite数据库操作

def main():
    baseurl = 'http://movie.douban.com/top250?start='
    askURL("http://movie.douban.com/top250?start=")
    datalist = getData(baseurl)
    savepath = r'D:\pycharm\project\cangku01\data.xlsx'


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i * 25)
        xinxi = askURL(url)
    return datalist

# 得到指定一个URL的网页内容
def askURL(url):
    # 告诉网页设备信息，模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
    }
    # 访问请求
    qq = urllib.request.Request(url=url, headers=headers)
    try:
        #相应
        xy = urllib.request.urlopen(qq,timeout = 5)
        xinxi = xy.read().decode('utf8')
        print(xinxi)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return xinxi

# 保存数据
# def saveData(savepath):

# +++++++++++++++++++++++++++++++++++++++++++++++
# 🔥 🔥 🔥 就是少了这一句！！！
# +++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    main()