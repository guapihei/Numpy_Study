#-*- coding = utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import openpyxl
import time

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)  # 爬取数据
    savepath = r"D:\pycharm\project\cangku01\data.xlsx"  # excel用xlsx
    saveData(datalist, savepath)  # 保存数据（必须调用！）
    print("全部保存完成！")

# 爬取网页
def getData(baseurl):
    datalist = []

    for i in range(0, 10):  # 10页，每页25条
        url = baseurl + str(i * 25)
        html = askURL(url)  # 获取网页源码

        # 解析数据,使用html.parser解析器
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []
            item = str(item)

            # 电影名称
            title = re.findall(r'<span class="title">(.*?)</span>', item)[0]
            data.append(title)

            # 评分
            score = re.findall(r'<span class="rating_num".*?>(.*?)</span>', item)[0]
            data.append(score)

            # 评价人数
            judgeNum = re.findall(r'<span>(\d+)人评价</span>', item)[0]
            data.append(judgeNum)

            datalist.append(data)

        time.sleep(1)  # 延迟1秒，防止被封

    return datalist

# 得到指定URL的网页内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=5)
        html = response.read().decode("utf-8")
        return html
    except Exception as e:
        print(e)
        return ""

# 保存数据到Excel
def saveData(datalist, savepath):
    # 创建工作簿
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "豆瓣TOP250"

    # 表头
    ws.append(["电影名称", "评分", "评价人数"])

    # 写入数据
    for data in datalist:
        ws.append(data)

    wb.save(savepath)

# 程序入口
if __name__ == "__main__":
    main()