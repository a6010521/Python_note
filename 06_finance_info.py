import requests
import pandas as pd

def get_finance():
    url = "https://rate.bot.com.tw/xrt/flcsv/0/day"

    response = requests.get(url)
    response.encoding = "utf-8"
    
    # 轉換為列表
    lines = response.text.strip().split("\n")
    
    # 解析 CSV，處理每行的欄位數量
    data = []
    for line in lines:
        columns = line.split(",")
        # 檢查欄位數量是否一致，若不一致，補齊缺失欄位
        if len(columns) == 22:  # 假設正確的列數是 22
            data.append(columns)
        else:
            # 若欄位數量不對，加入 None 或空白來補齊
            columns += [None] * (22 - len(columns))
            data.append(columns)
    
    # 生成 DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # 第一行當標題
    
    # 存成 CSV 檔案
    df.to_csv("exchange_rate.csv", index=False, encoding="utf-8")
    print("CSV 儲存完成")

get_finance()
