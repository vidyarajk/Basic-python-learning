### 1D array
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr.shape)

###convert 1D to 2D array
arr1=np.array([1,2,3,4,5])
arr1=arr1.reshape(1,5)
print(arr1)
print(arr1.shape)

arr1=np.array([1,2,3,4,5])
arr1=arr1.reshape(5,1)
print(arr1)
print(arr1.shape)

arr2=np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(arr2)
print(arr2.shape)

print((np.arange(0,10,2)).reshape(5,1))

### all elements are one
print(np.ones((3,5)))

### identity matrix
print(np.eye(3))
