import requests
from bs4 import BeautifulSoup

url ="https://www.104.com.tw/company/10zmukgg?jobsource=index_s_cs"

headers = {
    "User-Agnet" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

if response.status_code == 200:
    print("good!!!!!")
else:
    print("shittttt")

soup = BeautifulSoup(response.text, "html.parser")


job = soup.select('#joblist > div:nth-child(2) > div:nth-child(1) > a > div > div:nth-child(1) > div > div:nth-child(2)')
print(job)


