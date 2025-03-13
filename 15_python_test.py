from bs4 import BeautifulSoup
import requests
import time


def get_muji_info():
    
    url = "https://www.muji.com/tw/events/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    retries = 3
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            print(f"{response.status_code}請求成功")
            print(soup)
            break
        except Exception as e:
            print(f"發生錯誤: {e}")
            time.sleep(3)

get_muji_info()







