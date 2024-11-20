#1D aaray mein axis 1 hogi ie. [Axis 0]
#2D aaray mein axis 2 hogi ie. [Axis 0, Axis 1]
#  eg for 2D axis:   c1 c2 c3
#                r1[[ 1, 2, 3]
#                r2 [ 4, 5, 6]        
#                r3 [ 7, 8, 9]]        
#hence the sum of Axis 0 will be sum of rows intersecting [1+4+7 , 2+5+8 , 3+6+9] = [12,15,18]
#  and the sum of Axis 1 will be sum of columns intersecting [1+2+3 , 4+5+6 , 7+8+9] = [6,15,24]  

import numpy as np

x= [[1,2,3] , [4,5,6] , [7,8,9]]
arr = np.array(x)
print(arr)
print()

print("Sum for Axis 0: ")
print(arr.sum(axis=0))
print("Sum for Axis 1: ")
print(arr.sum(axis=1))
print()

print(arr.T) #transpose
print()

print(arr.flat) #we get an iterator 
for item in arr.flat:
    print(item)
print()

print(arr.ndim) #gives the number of dimensions
print(arr.size) #9
print(arr.nbytes) #shows the total bytes consumed 

one = np.array([1,3,5,600,2])
print(one.argmax()) #sabse bade element ki index
print(one.argmin()) #sabse chote element ki index
print(one.argsort()) #sort karega from small to large
print()

print(arr.argmax()) #as the max value (ie. 9) is at index 8
print(arr.argmin()) #as the min value (ie. 1) is at index 0
print(arr.argmax(axis=0)) #har column ka max index show krega
print(arr.argmin(axis=1)) #har column ka min index show krega
print(arr.argsort(axis=1)) 
print(arr.argsort(axis=0))
print()

print(arr.ravel())
print(arr.reshape(9,1))