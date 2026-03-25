#-*- codeing = utf-8 -*-

from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，文字匹配
import urllib.request,urllib.error #制定URL
import openpyxl #进行excel操作
import sqlite3 #进行SQLite数据库操作

def main():
    baseurl = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1"
    datalist = getData(baseurl)  # 爬取数据
    savepath = r"D:\pycharm\project\cangku01\data.xlsx" #存储位置
    saveData(datalist, savepath)
    print("全部保存完成！")


# 爬取网页
def getData(baseurl):
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    # 1. 定位到包含所有分类的父容器
    category_container = soup.find("div", id="search_all_category")
    # 2. 提取所有分类链接 (a标签)
    category_links = category_container.find_all("a", attrs={"dd_name": True})
    # 3. 遍历提取数据
    category_list = []
    for link in category_links:
        category_info = {}

        # 提取分类名称 (显示文字)
        #category_name = link.get_text(strip=True)

        # 提取分类ID (dd_name属性)
        # 注意：有些a标签可能没有dd_name，没有置为空
        category_id = link.get("dd_name", "")

        category_list.append([category_id])
    return category_list

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
        xinxi = xy.read().decode('gbk')
        #print(xinxi)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return xinxi

# 保存数据到Excel
def saveData(datalist, savepath):
    #创建一个新的Excel文件
    wb = openpyxl.Workbook()
    #打开Excel里面的sheet1
    ws = wb.active
    #sheet1名字
    ws.title = "当当网标签栏"
    #写入表头
    ws.append(["全部分类"])

    for data in datalist:
        ws.append(data)
    wb.save(savepath)

# +++++++++++++++++++++++++++++++++++++++++++++++
# 🔥 🔥 🔥 就是少了这一句！！！
# +++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    main()