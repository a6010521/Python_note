import requests
from bs4 import BeautifulSoup
import pandas as pd

# 執行後可以取得 << TVBS-REALNEWS >>
url = "https://news.tvbs.com.tw/realtime"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

if response.status_code == 200:
    print("good!!!")
else:
    print("shittttt", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# 取得所有標題和分類資料
news = soup.select("h2.txt")  # 標題
title = soup.select("div.type")  # 分類

# 初始化空的列表
titles_list = []
text_list = []

# 逐行提取資料並放入列表
if news and title:
    for elements, content in zip(news, title):
        text = elements.text.strip()
        titles = content.text.strip()

        # 將資料加入列表
        titles_list.append(titles)
        text_list.append(text)

        print(f"{titles}分類 | {text}")
        print("-------")
else:
    print("沒有找到該標籤")

# 創建 DataFrame
news_data = pd.DataFrame({
    "新聞分類": titles_list,
    "新聞標題": text_list
})

# 顯示結果
print(news_data)
news_data.to_excel('today_tvbs_news.xlsx', index=False)
