import httpx
import json
import time
from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from datetime import timedelta
from prefect.server.schemas.schedules import IntervalSchedule

# === 1. 取得最新的 ID 清單 ===
@task
def fetch_ids():
    """模擬從資料庫或 API 取得最新 ID 清單"""
    ids = [f"data_{i}" for i in range(1, 2500)]  # 假設 2500 筆資料，每天可能會更新
    return ids

# === 2. 保存爬取進度 ===
@task
def save_progress(last_index: int):
    with open("progress.json", "w") as f:
        json.dump({"last_index": last_index}, f)

@task
def load_progress():
    """讀取上次爬取的進度"""
    try:
        with open("progress.json", "r") as f:
            progress = json.load(f)
            return progress.get("last_index", 0)
    except FileNotFoundError:
        return 0  # 如果沒有記錄，從 0 開始

# === 3. 爬取數據 ===
@task
def fetch_data(data_id: str):
    """模擬爬取數據"""
    url = f"https://example.com/api/data/{data_id}"
    response = httpx.get(url)
    return response.json()

# === 4. 存儲數據 ===
@task
def save_data(data):
    """模擬存入資料庫或 CSV"""
    with open("results.json", "a") as f:
        json.dump(data, f)
        f.write("\n")  # 每行存一筆數據

# === 5. 主流程 ===
@flow(task_runner=SequentialTaskRunner)
def crawl_task():
    ids = fetch_ids()  # 取得最新 ID
    last_index = load_progress()  # 讀取上次進度
    max_requests_per_day = 1000  # API 限制

    # 如果上次進度超過 ID 總數，表示全部爬完，從頭開始
    if last_index >= len(ids):
        print("爬取完成，從第一筆重新開始")
        last_index = 0

    # 計算當次爬取範圍
    start = last_index
    end = min(last_index + max_requests_per_day, len(ids))

    for i in range(start, end):
        data = fetch_data(ids[i])  # 爬取數據
        save_data(data)  # 存儲結果
        save_progress(i + 1)  # 保存爬取進度
        time.sleep(1)  # 限制請求頻率

    print(f"今日爬取完成，共處理 {end - start} 筆，明天繼續")

# === 6. 設定 Prefect 排程，每 24 小時執行一次 ===
if __name__ == "__main__":
    from prefect.deployments import Deployment

    deployment = Deployment.build_from_flow(
        flow=crawl_task,
        name="daily_crawler",
        schedule=IntervalSchedule(interval=timedelta(days=1))
    )
    deployment.apply()
