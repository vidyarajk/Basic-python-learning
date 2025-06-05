import pandas as pd
data=pd.read_csv("cereal.csv")
print(data)

grpd_mean=data.groupby("mfr")['fiber'].mean() # grouping based on one category
print(grpd_mean)

grp=data.groupby(["mfr","rating"])['vitamins'].sum() # grouping based on 2 category
print(grp)

grpd=data.groupby("mfr")['rating'].agg(['mean','sum','count']) # aggregation by multiple function
print(grpd)