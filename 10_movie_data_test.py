import requests  
import pandas as pd
import math
import time


def get_movie_id():
    movie_id_raw = pd.read_csv("deatail路徑")
    movie_id_list = movie_id_raw["movie_id"].tolist()
    movie_id = [movie_id for movie_id in movie_id_list if not (isinstance(movie_id, float) and math.isnan(movie_id))]
    movie_id_len = (len(movie_id))
    return movie_id, movie_id_len


def data_movie_info(movie_id):

    api_token = "de467a5d"
    max_requests = 1000
    count_requests = 0
    start_time = 0
    end_time = 1000

    results = []
    try:
        for i in (start_time, end_time):
            
            #幫我建立一個try判斷如果抓不到資料後就跳出#
            
            for movie_info in movie_id:

                if count_requests >= max_requests:
                    break

                url = f"http://www.omdbapi.com/?i={movie_info}&apikey={api_token}"
                headers = {
                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
                }

                response = requests.get(url, headers=headers)
                print(f"正在抓取第{count_requests+1}筆")

                if response.status_code == 200:
                    data = response.json()
                    results.append(data)
                    count_requests += 1
                    start_time += 1000
                    end_time += 1000
                    print(f"成功請求{movie_info+1}")

                    time.sleep(86410)

                else:
                    print(f"無法請求{movie_info}")
    except requests.exceptions.RequestException as e:
        print(f'發生錯誤: {e}')
    
    return results


id, count = get_movie_id()
data_movie_info(id)


    

    
