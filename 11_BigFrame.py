"""
語法來自github googleapis
git clone gh repo clone googleapis/python-bigquery-dataframes
file : pandas_methods_test.py
官方文件 : https://cloud.google.com/python/docs/reference
"""
"""
下載套件
pip install --upgrade bigframes
"""
"""
Google Cloud 的身份驗證機制（例如 gcloud auth 或 Application Default Credentials)
in cmd or power shell(mac in terminal)
gcloud auth application-default login
^^^^如果是在雲端操作有其他做法^^^^
"""
"""
設配額/環境變數
unxi >> export GOOGLE_CLOUD_PROJECT= "PROJECT_ID"
win >> set GOOGLE_CLOUD_PROJECT= "your-project-id"
"""
"""
如果仍無法讀取可確認GOOGLE CLOUD認證 & INSTALL下面這段
pip install --upgrade bigframes pandas
"""
#抓取csv&json語法差異不大，其餘的調整去找chatgpt or 上面的官方文件
import bigframes.pandas as bpd

#-----------------------------你的project name
bpd.options.bigquery.project = "my-project-7393-451114"
def test_query():
    #------------- 可以去BigQuery複製sql語法from後面那段
    first_query = "my-project-7393-451114.001test.001-test" 

    try:
        # 嘗試讀取 BigQuery 資料
        movie_query = bpd.read_gbq(first_query)
        
        # 檢查是否成功
        if movie_query is not None:
            print("Data loaded successfully!")
            print(movie_query.head(5))  # 前 5 筆
        else:
            print("Failed to load data.")
    except Exception as e:
        print(f"Error occurred: {e}")

# 呼叫測試函式
test_query()