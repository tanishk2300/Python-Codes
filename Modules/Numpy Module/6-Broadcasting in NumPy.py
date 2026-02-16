import numpy as np 

arr=np.array([1,2,3,4])
result=arr+10 # broadcasting : 10 is added to all element .
print(result) # output=[11,12,13,14]


#________________________________________

arr1=np.array([[1,2,3],[5,6,7]])
arr2=np.array([1,2,3])
result=arr1+arr2# broadcasting arr1 accros to arr2.
print(result)

#_________________________________________


# Simulating a dataset (5 samples, 3 features)
data = np.array([[10, 20, 30],
                 [15, 25, 35],
                 [20, 30, 40],
                 [25, 35, 45],
                 [30, 40, 50]])

# Calculating mean and standard deviation for each feature (column)
mean = data.mean(axis=0)
std = data.std(axis=0)

# Normalizing the data using broadcasting
normalized_data = (data - mean) / std

print(normalized_data)