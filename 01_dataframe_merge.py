import pandas as pd
from functools import reduce


# 第一個 DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})

# 第二個 DataFrame
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 90000, 100000]
})
#表單join以id為條件
merge_data = pd.merge(df1, df2, on="ID", how="outer")
print(merge_data)
print("---------------")

#指定欄位進行排序
merge_data2 = merge_data.sort_values("Age", ascending=False)
print(merge_data2)



#定義可接收多個dataframe的func
def data_merge(key, *dfs):
     #reduce遞迴
     return reduce(lambda left, right: pd.merge(left, right, on=key), dfs)

df1 = pd.DataFrame({'ID': [1, 2, 3], 'A': ['a1', 'a2', 'a3']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'B': ['b1', 'b2', 'b3']})
df3 = pd.DataFrame({'ID': [1, 2, 3], 'C': ['c1', 'c2', 'c3']})
df4 = pd.DataFrame({'ID': [1, 2, 3], 'd': ['d1', 'd2', 'd3']})


merged_df = data_merge('ID', df1, df2, df3, df4)


print(merged_df)

