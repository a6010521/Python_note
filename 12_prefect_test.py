import httpx
import json
import math
import pandas as pd
import time

from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from datetime import timedelta
from prefect.server.schemas.schedules import IntervalSchedule

"""取得id清單"""
@task
def get_id_list() -> list:
    #讀取csv，取id，去nan值
    movie_id_csv = pd.read_csv("檔案路徑")
    movie_id_list = movie_id["imdb_id"].tolist()
    movie_id = [movie_id for movie_id in movie_id_list if not (isinstance(movie_id, float) and math.isnan(movie_id))]
    movie_id_len = len(movie_id)
    return movie_id, movie_id_len

"""保存爬取的進度"""
@task
def save_data(last_index: int):
    try:
        with open("omdb_info.json", "w") as f:
            json.dump({"last_index": last_index}, f)

"""讀取爬取進度"""
@task
def load_data()
    try:
        with open("omdb_info.json", "r") as f:
            progress = json.load(f)
            return progress.("last_index", 0)
    except FileNotFoundError:
        return 0
                

"""爬蟲碼"""
@task
def omdb_requests():
