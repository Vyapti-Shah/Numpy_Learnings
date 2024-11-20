import numpy as np
myArr = np.array([[3,6,32,7]], np.int8) #here [[]] double square brackets show it is a 2D array
                                      #here int8 shows the memory we have taken for the data for larger numbers 
                                      #we can also increase the bit rom 8 to 16 to 32 and so on
print(myArr)
print(myArr[0])
print(myArr[0,1])
print(myArr.shape)
print(myArr.dtype)

myArr[0,3] = 45
print(myArr)
