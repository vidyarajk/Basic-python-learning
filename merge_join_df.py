import pandas as pd

data1={
    "key":["a","b","c"],
    "value":[2,3,4]
}

data2={
    "key":["a","b","d"],
    "value":[1,2,3]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)

a=pd.merge(df1,df2,on="key",how="outer")
s=pd.merge(df1,df2,on="key",how="inner")
d=pd.merge(df1,df2,on="key",how="left")
f=pd.merge(df1,df2,on="key",how="right")

print(a)
print(s)
print(d)
print(f)