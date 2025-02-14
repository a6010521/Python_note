import requests
from bs4 import BeautifulSoup

#執行後可以取得<<   拓 元   >>目前全部節目   
url = "https://tixcraft.com/activity"

headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
if response.status_code == 200 :
    print("good!!!")
else:
    print("shittttt")
#解析網站的html
soup = BeautifulSoup(response.text, "html.parser")

date = soup.select("[class^='date']")

title = soup.select("[class^='multi_ellipsis']")

href = soup.select("#all > div:nth-child(2) > div:nth-child(1) > div > a")

paired_data_dict = {}

if len(date) == len(title):
    for i in range(len(date)):
        # 使用索引作為鍵，日期作為值，標題作為值
        paired_data_dict[date[i].text.strip()] = title[i].text.strip()

    # 輸出字典
    for date, title in paired_data_dict.items():
        print(f"Date: {date} - Title: {title}")
        print("-----------------------")
else:
    print("日期和標題的數量不匹配！")








    