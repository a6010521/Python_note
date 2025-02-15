import requests 
import pandas as pd
from bs4 import BeautifulSoup

def finance_requests():

    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.encoding="utf-8"

    if response.status_code == 200:
        print("good")
    else:
        print("fail")

    soup = BeautifulSoup(response.text, "html.parser")

    finance_table = soup.select("#ie11andabove > div > table")

    if finance_table:
        print("成功找到表格！")
          # 顯示表格 HTML 結構
    else:
        print("無法找到匯率表格！")

    rows = finance_table[0].find_all("tr")  # 找出所有列
    for row in rows:
        columns = row.find_all("td")  # 找出所有欄位
        data = [col.text.strip() for col in columns]  # 提取文字
        print(data)

    

finance_requests()