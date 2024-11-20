import numpy as np

arr1 = np.array([[1,2,3],[4,5,0],[0,1,0]])
arr2 = np.array([[1,0,3],[4,2,0],[1,0,2]])
print(arr1 + arr2)
print(arr1 * arr2)
print(np.sum(arr1))
print(np.max(arr1))
print(np.min(arr1))
print(np.where(arr1>3)) #shows at which indexes arr1 has a value grater than 3
print(type(np.where(arr1>3))) #arrays la tuple bnake return kiya
print(np.count_nonzero(arr1)) #counts the places that have non zero value
print(np.nonzero(arr1)) #states the places where non xero value is present
print()

arr1[0,2] = 0
print(np.nonzero(arr1))

import sys
py_arr = [0,4,55,2]
np_arr = np.array(py_arr)
print(sys.getsizeof(1)*len(py_arr))  #gives py elemnt ka size
print(np_arr.itemsize * np_arr.size) #gives np elemnt ka size
#this shows that numpy takes less memory than py