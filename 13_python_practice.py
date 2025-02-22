import pandas as pd

# 創建 DataFrame
data = {
    'ID': range(1, 31),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack', 
             'Kate', 'Leo', 'Mona', 'Nina', 'Oscar', 'Paul', 'Quincy', 'Rita', 'Sam', 'Tina', 
             'Uma', 'Victor', 'Wendy', 'Xander', 'Yara', 'Zane', 'Aaron', 'Bella', 'Cindy', 'Dan'],
    'Age': [53, 47, 57, 52, 31, 38, 29, 45, 51, 42, 
            34, 28, 39, 50, 44, 32, 41, 49, 36, 48, 
            33, 40, 55, 46, 30, 37, 56, 43, 52, 58],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
             'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Indianapolis', 'Charlotte', 
             'San Francisco', 'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Detroit', 'Nashville', 
             'Portland', 'Memphis', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore'],
}

emp_df = pd.DataFrame(data)

# 顯示 DataFrame
total_age = emp_df['Age'].sum()
print(total_age)

total_people = emp_df.shape[0]
print(total_people)

import json



