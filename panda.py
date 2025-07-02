import pandas as pd
## series
data=[1,2,3,4,5]
print(pd.Series(data))

## series formation using dictinary
dict={1:"a",2:"b",3:"c"}
print("Dictionary series:\n", pd.Series(dict))

data1=[1,2,3,4]
index=["q","w","e","r"]
print(pd.Series(data1,index=index))

## dataframe
data2={
    "name":["vidya","roshin","yuvram"],
    "age":[33,35,5],
    "city":["kannur","malprm","kozhikode"]
    }
df=pd.DataFrame(data2)
print(df)

### dataframe using list of dictionaries
data3=[
    {"name":"vidya","age":33,"city":"blr"},
    {"name":"yuvram","age":5,"city":"mlr"},
    {"name":"roshin","age":35,"city":"bhyd"}
]
df=pd.DataFrame(data3)
print(df)

df1=pd.read_csv("BigMartSalesData.csv")
print(df1.head(5))  ### first 5
print(df1.tail(5))  ### last 5
print(df['name'])   ### to get name column
print(df.loc[1])    ### to get the row
print(df.loc[0][2])
print(df.iloc[0][0]) ### integer posiiton