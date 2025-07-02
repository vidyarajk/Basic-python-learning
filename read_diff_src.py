import pandas as pd
from io import StringIO
data=data = '''
[
  {"name": "Alice", "age": 25, "city": "Delhi"},
  {"name": "Bob", "age": 30, "city": "Mumbai"},
  {"name": "Charlie", "age": 35, "city": "Chennai"}
]
'''
df=pd.read_json(StringIO(data)) ### json to dataframe
print(df)

print(df.to_json())  ### back to json based on index same as df.to_json(orient="index")
print(df.to_json(orient="index"))

print(df.to_json(orient="records")) ### based on record

### read_csv using url
df1=pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv",header=None)
print(df1)

df1.to_csv("sample.csv") ## back to csv

### read html file
url = "https://www.w3schools.com/html/html_tables.asp"
df2=pd.read_html(url,header=0)
print(df2)

## read excel file
df3=pd.read_excel("sample_data.xlsx")
print(df3)
df3.to_pickle('df_excel')
print(pd.read_pickle('df_excel'))


