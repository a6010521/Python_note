import pandas as pd

#讀取檔案
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')

#存取檔案
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json', orient='records')

#語法筆記
df.head()        # 查看前 5 行
df.tail()        # 查看後 5 行
df.info()        # 查看 DataFrame 資訊
df.describe()    # 統計摘要
df.shape        # 查看 DataFrame 形狀 (行數, 列數)
df.columns      # 查看欄位名稱
df.dtypes       # 查看欄位型別
df.isnull().sum()  # 檢查缺失值

#選取單列、欄
df['Name']  # Series
df[['Name', 'Age']]  # DataFrame


df.iloc[0]  # 第一行 (基於索引)
df.loc[0]   # 第一行 (基於標籤)

df.iloc[1:3]  # 選擇第 2~3 行 (索引)
df.loc[1:3]   # 選擇標籤為 1~3 的行

#條件篩選
# 年齡大於 30
df[(df['Age'] > 25) & (df['Salary'] > 50000)]  # 多重條件
df[df['Name'].str.contains('Ali')]  # 字符串篩選


#新增欄位
df['Bonus'] = df['Salary'] * 0.1
#修改欄位
df.loc[df['Name'] == 'Alice', 'Age'] = 26
#刪除欄位
df.drop(columns=['Bonus'], inplace=True)
#刪除行
df.drop(index=[0, 2], inplace=True)


#排序
df.sort_values(by='Age', ascending=False, inplace=True)
#群組
df.groupby('Age').mean()
df.groupby('Age').agg({'Salary': 'sum', 'Bonus': 'mean'})

#nan值處理
df.dropna()  # 刪除缺失值
df.fillna(0)  # 用 0 填補缺失值
df.fillna(df.mean())  # 用平均值填補

#"列"合併
df_new = pd.concat([df1, df2], axis=0)
#"欄"合併
df_new = pd.merge(df1, df2, on='Name', how='inner')  # 交集
df_new = pd.merge(df1, df2, on='Name', how='outer')  # 聯集

#欄位型態轉換
df['Age'] = df['Age'].astype(float)  # 轉換為浮點數
#日期轉換
df['Date'] = pd.to_datetime(df['Date'])

#計算唯一值數量
df['Name'].nunique()
df['Name'].value_counts()


#建立新索引
df.set_index('Name', inplace=True)
df.reset_index(inplace=True)

#forloop >> dataframe
for index, row in df.iterrows():
    print(row['Name'], row['Age'])

#可迭代多個list
for j, k, c in zip(Name, Age, City):
    print(f"Name: {j}, Age: {k}, City: {c}")