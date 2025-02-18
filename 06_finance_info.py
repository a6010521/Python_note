import requests
from bs4 import BeautifulSoup

def get_finaace():

    url = "https://tw.stock.yahoo.com/class-quote?sectorId=40&exchange=TAI"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    if response.status_code == 200:
        print("good")
        div_element = soup.find_all("div", class_="Lh(20px) Fw(600) Fz(16px) Ell")
        
        for div_elements in div_element:
            title = div_elements.text
            print(title)
       

    else:
        print("fail")

    

    
get_finaace()