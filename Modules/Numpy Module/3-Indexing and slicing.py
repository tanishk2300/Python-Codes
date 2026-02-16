import numpy as np 

#_____Indexing (Same as Python Lists)_____
arr1=np.array([10,20,30,40])
print(arr1[0])#output=10
print(arr1[-1])#output=40

#____Slicing (Extracting Parts of an Array)_____
arr2 = np.array([10, 20, 30, 40, 50])
print(arr2[1:4])#output=20 30 40] (slice from index 1 to 3).
print(arr2[-1:])#output=[50].
print(arr2[::2])#output=[10 30 50].

#Slicing returns a view, not a copy! Changes affect the original array.**
#Use .copy() if you need an independent copy.
sliced = arr2[1:4]# (here .copy() is used like [arr2.copy()] ) # this will choose the range like 20,30,40,50 and append at the place of 20 becouse of sliced[0] it let the value at possition 1 will be zero . 
sliced[0]=999 #this help to append the 999 in the arr2 at btw [1:4] and the 1 will be 0 converted by sliced[0].
print(arr2)#output=[10 999 30 40 50]

# _____Fancy Indexing & Boolean Masking____
# Fancy Indexing (Select Multiple Elements)
arr3=np.array([10, 20, 30, 40, 50])
idx=[0,2,4]# Indices to select.
print(arr3[idx])#output= [10 30 50]

#Boolean Masking (Filter Data)
arr4 = np.array([10, 20, 30, 40, 50])
mask = arr4 > 25  # Condition: values greater than 25
print(arr4[mask])  # [30 40 50]