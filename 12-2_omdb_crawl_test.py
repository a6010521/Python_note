import math
import pandas as pd
import requests
import time

def fetch_imdb_id():  
    #路徑會可能來自gcs
    movie_id_csv = pd.read_csv(r"tmdb_detail_raw.csv")
    movie_id_list = movie_id_csv["imdb_id"].tolist()   
    #去除nan值
    movie_id = [movie_id for movie_id in movie_id_list if not (isinstance(movie_id, float) and math.isnan(movie_id))]
    
    return movie_id

API_TOKEN = "de467a5d"

def crawl_movies_data(movie_id, API_TOKEN):

    max_request = 1000
    count_requests = 0
    results = []
    exsiting_id = []

    for id in movie_id:
        if count_requests >= max_request:
            print(f"已請求{max_request}次請求，今日結束")
            break
            

        url = f"http://www.omdbapi.com/?i={id}&apikey={API_TOKEN}"
        headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            movie_info = response.json()
            results.append(movie_info)
            exsiting_id.append(id)
            
        else:
            print("爬取失敗")
        
        count_requests += 1
        time.sleep(2)

    return results, exsiting_id

movie_id = fetch_imdb_id()
data, exitid = crawl_movies_data(movie_id, API_TOKEN)
print(data)
print(exitid)

    



