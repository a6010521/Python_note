import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# 執行後可以取得 << TVBS-REALNEWS >>
def get_news():
    
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

            #print(f"{titles}分類 | {text}")
            #print("-------")
    else:
        print("沒有找到該標籤")

    # 創建 DataFrame
    news_data = pd.DataFrame({
        "新聞分類": titles_list,
        "新聞標題": text_list
    })
    #新增日期欄位
    news_data["日期"] = datetime.today().strftime("%Y-%m-%d") 
    news_data["日期"] = pd.to_datetime(news_data["日期"])
    #創建資料建立時間儲存指定路徑
    current_time = datetime.now().strftime("%Y-%m-%d")
    #儲存指定路徑
    save_path = "C:\\Users\\User\\Desktop\\Python_note\\01-news_folder"   
    file = os.path.join(save_path, f"{current_time}_news.csv")
    news_data.to_csv(file, index=False)
    

    return news_data

#result = get_news()


#指定篩選欄位閱讀
def read_news():
    #讀取指定路徑
    file_path = r"C:\Users\User\Desktop\Python_note\01-news_folder\2025-03-14_news.csv"
    #讀取csv
    news_data = pd.read_csv(file_path)
    #計算有幾種新聞種類
    news_type_counts = news_data['新聞分類'].value_counts()
    #指定分類新聞
    entertainment_news = news_data[news_data['新聞分類'] == '娛樂']
    
    return news_type_counts

info = read_news()
print(info)


    