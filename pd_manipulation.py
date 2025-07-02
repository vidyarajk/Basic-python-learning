import pandas as pd
data=[
    {"Name":"vidya","age":33,"city":"tvm"},
    {"Name":"roshhin","age":35,"city":"blr"},
    {"Name":"yuv","age":5,"city":"mlr"}
    ]
df=pd.DataFrame(data)
print(df)

### added a new column salary
df["salary"]=[30000,50000,20000]
print(df)

### to remove a column temporarly
df.drop('salary',axis=1) 
print(df)

print(len(df))

# Add a new row
df.loc[len(df)] = ['bhavya', 38, 'tvm',40000] #### using loc[len[df]]

new_row = pd.DataFrame([{'Name': 'kavya', 'age': 34, 'city': 'mnm','salary':42000}])
df = pd.concat([df, new_row], ignore_index=True) #### using concat function

print(df)
### to remove a column permanently
df.drop('salary',axis=1,inplace=True) 
print(df)

### add age by 1
df['age']=df['age']+1
print(df)

