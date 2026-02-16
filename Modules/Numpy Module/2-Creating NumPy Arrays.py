import numpy as np 
#1D array
arr=np.array([2,3,4]) # this is 1D array . 
print(arr)
#2D array
arr1=np.array([[1,2,3],[5,6,7]])# this is a 2D array . 
print(arr1)
#zeros are printed .
a=np.zeros((3,4))# this help to print the zeros according to 'np.zeros' in 3X4 matrix. 
print(a)
#ones is use to print 1 in matrix. 
b=np.ones((3,4))
print(b)
#here full is use to print the any number which you want to print in the matrix. 
c=np.full((4,6),7)
print(c)
#digonal matrix
d=np.eye((5))
print(d)
#arange help to make a list by add a number with the next and give result 
g=np.arange(1,100,2)
print(g)

f=np.linspace(0,1,5)#jab tak 1 nahi aajata tab tak 5 se divide hota rahega 0 se leke 1 tak answer aana chiye 5 se divide karne k baad . 
print(f)# [0. 0.25 0.5 0.75 1.] (evenly spaced)

#Checking Array Properties
arr = np.array([[10, 20, 30], [40, 50, 60],[70,80,90],[100,110,120]])# this is 4d array.
print("shape",arr.shape)# (4, 3) → 4 rows, 3 columns.
print("size",arr.size)# output = size 12 .
print("dimentions",arr.ndim)#output = dimentions 2
print("data type",arr.dtype)#output=int64

#___Changing Data Types____
arr=np.array([[1,2,34],[4,5,6]], dtype=np.float32)# this help to change the data type .
print(arr.dtype)# output= float32.


arr_int=arr.astype(np.int32) # Convert float to int

print(arr_int)#output=[[ 1  2 34][ 4  5  6]]

# ____Reshaping and Flattening Arrays_____
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)#output=(2, 3).

reshaped=arr.reshape(3,2) # Change shape.
print(reshaped)#output=[[1 2][3 4][5 6]].

flattened=arr.flatten()#Convert 2D → 1D.
print(flattened)#output=[1 2 3 4 5 6].

