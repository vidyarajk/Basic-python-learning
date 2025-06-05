import pandas as pd
df=pd.read_csv("BigMartSalesData.csv")
print(df.head(5))
print(df.isnull().sum()) ### count toatal null per column
print(df.dtypes)

df['CustomerID_fillmean']=df['CustomerID'].fillna(df['CustomerID'].mean())
print(df)

print(df.isnull().any()) ### if any null value exist in column

print(df[df['CustomerID'].isnull()]) ### Filter rows with nulls in a column

df=df.rename(columns={"InvoiceDate":"BillDate"}) #### rename the column
print(df.head(5))

df.drop("CustomerID_fillmean",axis=1,inplace=True) ### remove the column
print(df)

df['unit_price']=df['UnitPrice'].astype(int) ### changing the datatypes

print(df.dtypes)

df['unitprice']=df['unit_price'].apply(lambda x:x*2) ### apply lambda function

print(df)