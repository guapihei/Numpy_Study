#-*- codeing = utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import openpyxl
import gzip  # 新增：解压gzip
from io import BytesIO  # 新增：处理字节流

def main():
    baseurl = "https://www.bilibili.com/video/BV13yt6zXEsf/?spm_id_from=333.337.search-card.all.click&vd_source=7eb2e80582b323a4294420b95852810d"
    datalist = getData(baseurl)
    savepath = r"D:\pycharm\project\cangku01\data.xlsx"
    saveData(datalist, savepath)
    print("全部保存完成！")

def getData(baseurl):
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")

    info_blocks = soup.find_all("div", id="info")
    category_list = []

    for info in info_blocks:
        a_tag = info.find("a")
        username = "未知"
        if a_tag:
            for content in a_tag.contents:
                if isinstance(content, str) and content.strip():
                    username = content.strip().replace('"', "")
                    break

        level = "无"
        img_tag = info.find("img", src=re.compile(r"level_\d+\.svg"))
        if img_tag:
            match = re.search(r"level_(\d+)", img_tag["src"])
            if match:
                level = f"LV{match.group(1)}"

        category_list.append([username, level])

    return category_list

def askURL(url):
    import requests  # 自动导入
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": "buvid3=1F822C48-3A9F-FBB5-2680-3C9E9B7D023B99925infoc; b_nut=1745836199; _uuid=F83223410-10B49-5B97-FD12-F1B58C41731902889infoc; enable_web_push=DISABLE; enable_feed_channel=ENABLE; buvid4=1C13177B-7D27-3476-49BE-135D56A8730200513-025042818-lHXhlN1FMHzcagpIBWpHaQ%3D%3D; buvid_fp=db45ea35c0c3f97b54374428032a57a8; rpdid=|(umYJlk)lYl0J'u~Rl)JYkJ); LIVE_BUVID=AUTO2417465388255807; header_theme_version=OPEN; DedeUserID=6399656; DedeUserID__ckMd5=ed9dc9757bde353d; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; CURRENT_QUALITY=0; home_feed_column=5; PVID=2; hit-dyn-v2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQ1NzgwMTIsImlhdCI6MTc3NDMxODc1Mn0.nbavNKFtli6mYT2ucLJVA9kJ5r4_aTJREht38sNcTyE; bili_ticket_expires=1774577952; browser_resolution=2552-1282; SESSDATA=4c43f0e9%2C1789993633%2C52825%2A32CjBIR81N6fYfbfIjPigybFjPh9m5NUTg26SLvL6-ifgeDycdBKB-jYFb0cp1_PKY8_MSVlBUd3BnQlEtdE8xaU1QeFR1M0Y5OVhDZ1E5a05Fa1JGNnZDNVRQWnNhUTE1dlVLdWpJNmV1cFlIQWtxbVhXWDc5NXZzWFFEZXJBZ1llcjhmeUh0SlBBIIEC; bili_jct=eb002f04d9b255c247ac448a60c8ad79; sid=5f8gvyhx; bp_t_offset_6399656=1183996928728236032; CURRENT_FNVAL=4048; b_lsid=6BB34F38_19D29171527",
        "Referer": "https://www.bilibili.com/",
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.encoding = "utf-8"
        return res.text
    except Exception as e:
        print("请求失败", e)
        return ""

def saveData(datalist, savepath):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "B站用户信息"
    ws.append(["用户名", "等级"])

    for data in datalist:
        ws.append(data)

    wb.save(savepath)

if __name__ == "__main__":
    main()