import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


#取得資料
def ie_requests():
    url = "https://news.tvbs.com.tw/realtime"

    headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    if response.status_code == 200 :
        print("good!!!")
    else:
        print("shittttt")

    soup = BeautifulSoup(response.text, "html.parser")

    news = soup.select("h2.txt")

    news_list = []

    if news:
        for elenents in news:
            text = elenents.text.strip()
            news_list.append(text)
            
    else:
        print("沒有找到該標籤")
    #回傳資料出來
    return news_list
    
new_data = ie_requests()

for news in new_data:
    print(news)
    print("------------")
#處理成dataframe
def news_df(new_data):
    
    data = new_data
    news_df = pd.DataFrame(data, columns=["即時新聞"])
    news_df["日期"] = datetime.today().strftime("%Y-%m-%d") 
    news_df["日期"] = pd.to_datetime(news_df["日期"])
    news_df.to_csv('today_news.csv', index=False)
    return news_df

result = news_df(new_data)
print(result)
print(type(result))




