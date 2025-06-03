import numpy as np
arr=np.array([[1,2,3,4],[2,3,4,5],[4,5,6,7]])
print("\n",arr)

print(arr[2][3])
print(arr[:2])# 1st 2 rows
print(arr[1:]) # 2nd and 3rd row
print(arr[1:,1:3])
print(arr[0:,1:2])
print(arr[1:2])

## modify elements

arr[0][2]=5
print(arr)
arr[1:,2:3]=10
print(arr)

##Statistical operations

data=np.array([1,2,4,5])
mean=np.mean(data)
std_dvn=np.std(data)
norm=(data-mean)/std_dvn
print(norm)
print("variance",np.var(data))
print("median",np.median(data))

###Logical operation

df=np.array([1,2,3,4,5,6,7,8,9])
print(df[(df>5)])
print(df[(df>5) & (df<8)])
