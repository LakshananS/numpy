import numpy as np #Call numpy

print(np.__version__)  #find the numpy version

#create a matrix and slicing exapmles 

arr = np.array([[1,2,3],[4,5,6]], np.int32)

print(arr)
print(type(arr))


arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#reshape the matrix
arr3 = arr2.reshape(4,3)

#form the matrix
print(arr3)
#slicing
print(arr2[1:5]) 
