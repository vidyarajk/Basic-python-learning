import pandas as pd
data=[
    {"Name":"vidya","age":33,"city":"tvm"},
    {"Name":"roshhin","age":35,"city":"blr"},
    {"Name":"yuv","age":5,"city":"mlr"}
    ]
df=pd.DataFrame(data)
print(df)

### accessing a elament using at and iat
print(df.at[2,"city"]) 
print(df.iat[1,2])
