import requests
from bs4 import BeautifulSoup

def ptt_news():

    url = "https://www.ptt.cc/bbs/Gossiping/index.html"

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    cookies = {"over18": "1"}

    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        print("good")
    else:
        print("fail")
    
    soup = BeautifulSoup(response.text, "html.parser")

    ptt_titles = [title.text for title in soup.select("div.title a")]

    return ptt_titles



new_titles = ptt_news()
for title in new_titles:
    print(title)
    print("--------")