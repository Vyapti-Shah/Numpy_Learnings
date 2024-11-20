import numpy as np

#array creation methods

#1.Conversion from other Python structures (eg. lists, dictionaries, tuples)
listArr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(listArr)
print(listArr.shape)
print(listArr.dtype)
print(listArr.size)
print(np.array({0,1,2})) #dictionary

#2.Intrinsic numpy array creation objects (eg. arange, ones, zeros, etc.)
zeross = np.zeros((2, 5))
print(zeross)
print(zeross.dtype)
print(zeross.shape)
rng = np.arange(15) #it gives an array not list
print(rng)
lspace = np.linspace(1,50,10) # it gives equally spaced 10 elements between 1 to 50 
                              # 1 se 10 ke bichke equally spaced 10 elements dega
print(lspace)

emp = np.empty((4,6)) #random elements of any random value of 4,6 array
print(emp)

emp_like = np.empty_like(lspace) #kese bhi initialize kr skte hai ie. jis index pe jo rkhna chahte hai rkh skte hai 
print(emp_like)

ide = np.identity(45) #45×45 ka ek identity matrix dega
print(ide)
print(ide.shape)

arr = np.arange(99)
print(arr)
arr = arr.reshape(3,33)
print(arr)
#print(arr.reshape(3,31)) #3,31 is not possible as we have a range of 99 so only number divisible by 99 is possible
print()

arr = arr.ravel() #ravel makes it a 1D array
print(arr)
print(arr.shape)
