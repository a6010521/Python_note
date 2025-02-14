import requests
from bs4 import BeautifulSoup

#執行後可以取得<<   TVBS-REALNEWS   >>
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

if news:
    for elenents in news:
        text = elenents.text.strip()
        print(text)
        print("-------")
else:
    print("沒有找到該標籤")

