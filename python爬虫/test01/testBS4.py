import requests
import openpyxl

# ====================== 配置区域 ======================
BV = "BV1PzZhBgELb"  # 你要爬的视频BV号

# 你的Cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Cookie": "buvid3=1F822C48-3A9F-FBB5-2680-3C9E9B7D023B99925infoc; b_nut=1745836199; _uuid=F83223410-10B49-5B97-FD12-F1B58C41731902889infoc; enable_web_push=DISABLE; enable_feed_channel=ENABLE; buvid4=1C13177B-7D27-3476-49BE-135D56A8730200513-025042818-lHXhlN1FMHzcagpIBWpHaQ%3D%3D; buvid_fp=db45ea35c0c3f97b54374428032a57a8; rpdid=|(umYJlk)lY0J'u~Rl)JYkJ); LIVE_BUVID=AUTO2417465388255807; header_theme_version=OPEN; DedeUserID=6399656; DedeUserID__ckMd5=ed9dc9757bde353d; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; CURRENT_QUALITY=0; home_feed_column=5; PVID=2; hit-dyn-v2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzQ1NzgwMTIsImlhdCI6MTc3NDMxODc1Mn0.nbavNKFtli6mYT2ucLJVA9kJ5r4_aTJREht38sNcTyE; bili_ticket_expires=1774577952; browser_resolution=2552-1282; SESSDATA=4c43f0e9%2C1789993633%2C52825%2A32CjBIR81N6fYfbfIjPigybFjPh9m5NUTg26SLvL6-ifgeDycdBKB-jYFb0cp1_PKY8_MSVlBUd3BnQlEtdE8xaU1QeFR1M0Y5OVhDZ1E5a05Fa1JGNnZDNVRQWnNhUTE1dlVLdWpJNmV1cFlIQWtxbVhXWDc5NXZzWFFEZXJBZ1llcjhmeUh0SlBBIIEC; bili_jct=eb002f04d9b25c247ac448a60c8ad79; sid=5f8gvyhx; bp_t_offset_6399656=1183996928728236032; CURRENT_FNVAL=4048; b_lsid=6BB34F38_19D29171527",
    "Referer": "https://www.bilibili.com/"
}

save_path = r"D:\pycharm\project\cangku01\所有评论用户.xlsx"
# ======================================================

all_users = []
next_page = 0

print("开始爬取所有评论用户...\n")

while True:
    url = f"https://api.bilibili.com/x/v2/reply/main?next={next_page}&type=1&oid={BV}"

    try:
        data = requests.get(url, headers=headers, timeout=10).json()
    except:
        print("请求失败，结束")
        break

    # ===================== 修复：正确判断是否还有评论 =====================
    if "data" not in data or "replies" not in data["data"] or len(data["data"]["replies"]) == 0:
        print("✅ 已爬取全部评论！")
        break

    # 提取当前页用户
    for reply in data["data"]["replies"]:
        name = reply["member"]["uname"]
        level = reply["member"]["level_info"]["current_level"]
        all_users.append([name, f"LV{level}"])
        print(f"用户：{name} | LV{level}")

    next_page += 1  # 翻页

# ===================== 保存Excel =====================
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "评论用户"
ws.append(["用户名", "等级"])

for user in all_users:
    ws.append(user)

wb.save(save_path)
print(f"\n✅ 保存成功！共 {len(all_users)} 个用户")