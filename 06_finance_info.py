import requests
import pandas as pd
from bs4 import BeautifulSoup

# Yahoo 股市產業類股網址
url = "https://tw.stock.yahoo.com/class-quote?sectorId=40&exchange=TAI"

# 設定 headers 模擬瀏覽器請求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# 發送請求
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# 找到表格
table = soup.find("table")
if table:
    # 取得表頭
    headers = [th.text.strip() for th in table.find("thead").find_all("th")]
    
    # 取得表格內容
    rows = []
    for tr in table.find("tbody").find_all("tr"):
        cells = [td.text.strip() for td in tr.find_all("td")]
        rows.append(cells)
    
    # 轉成 DataFrame
    df = pd.DataFrame(rows, columns=headers)
    
    # 顯示 DataFrame
    print(df)
else:
    print("找不到表格")
    print(response.status_code)


    

    
