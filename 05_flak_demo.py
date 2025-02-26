from google.cloud import bigquery

# 初始化 BigQuery 客戶端
client = bigquery.Client()

# 設定資料集ID和資料表ID
dataset_id = "project_id.dataset_id"
table_id = "table_id"

# 指定要上傳的本地端 CSV 檔案路徑
file_path = "path/to/your/local_file.csv"

# 設定欄位型態
schema = [
    bigquery.SchemaField("column1", "STRING"),
    bigquery.SchemaField("column2", "INTEGER"),
    bigquery.SchemaField("column3", "FLOAT"),
    bigquery.SchemaField("column4", "DATE"),
]

# 設定 BigQuery 載入作業配置
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,  # 跳過標題行
    autodetect=False,      # 關閉自動偵測欄位型態
    schema=schema,         # 使用我們定義的欄位型態
)

# 開啟檔案並上傳到 BigQuery
with open(file_path, "rb") as file:
    load_job = client.load_table_from_file(
        file,
        dataset_id + '.' + table_id,
        job_config=job_config
    )

# 等作業完成
load_job.result()

print(f"File {file_path} loaded to {dataset_id}.{table_id}")


#------------------------------------------------------------------------------------------------


import json

def save_data():
    file = "檔案路徑"
    
    # 先讀檔
    with open(file, "r") as f:
        existing_data = json.load(f)
    
    # 加入新的資料
    existing_data.append("二次求取新增的資料")
    
    # 再存檔
    with open(file, "w") as f:
        json.dump(existing_data, f, indent=4)


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
import pandas as pd

# 讀取 CSV 檔案
dfA = pd.read_csv('fileA.csv')
dfB = pd.read_csv('fileB.csv')

# 假設兩個表格的 ID 欄位名稱都是 'ID'
# 找出 B 表中存在但 A 表中沒有的 ID
only_in_B = dfB[~dfB["ID"].isin(dfA["ID"])]

# 顯示 B 表中特有的資料
print("只在 B 表中的資料:")
print(only_in_B)

# 儲存到新的 CSV 檔案
only_in_B.to_csv('only_in_B.csv', index=False)






