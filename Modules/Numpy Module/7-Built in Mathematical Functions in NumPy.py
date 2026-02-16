import numpy as np 

arr=np.array([1,2,3,4,5])
arr1=np.array([1,2,3,4])
arr2=np.array([6,7,8,9])
#_____np.mean() – Compute the mean (average) of an array.
mean=np.mean(arr)
print(mean)
#_____np.std() – Compute the standard deviation of an array.
std=np.std(arr)
print(std)
#_____np.var() – Compute the variance of an array.
var=np.var(arr)
print(var)
#_____np.min() – Compute the minimum value of an array.
min=np.min(arr)
print(min)
#_____np.max() – Compute the maximum value of an array.
max=np.max(arr)
print(max)
#_____np.sum() – Compute the sum of all elements in an array.
sum=np.sum(arr)
print(sum)
#_____np.prod() – Compute the product of all elements in an array.
prod=np.prod(arr)
print(prod)
#_____np.median() – Compute the median of an array.
median=np.median(arr)
print(median)
#_____np.percentile() – Compute the percentile of an array.
percentile=np.percentile(arr, 50)  # For the 50th percentile (median)
print(percentile)
#_____np.argmin() – Return the index of the minimum value in an array.
argmin=np.argmin(arr)
print(argmin)
#_____np.argmax() – Return the index of the maximum value in an array.
argmax=np.argmax(arr)
print(argmax)
#_____np.corrcoef() – Compute the correlation coefficient matrix of two arrays.
corrcoef=np.corrcoef(arr1, arr2)
print(corrcoef)
#_____np.unique() – Find the unique elements of an array.
unique=np.unique(arr)
print(unique)
#_____np.diff() – Compute the n-th differences of an array.
diff=np.diff(arr)
print(diff)
#_____np.cumsum() – Compute the cumulative sum of an array.
cumsum=np.cumsum(arr)
print(cumsum)
#_____np.linspace() – Create an array with evenly spaced numbers over a specified interval.
linspace=np.linspace(0, 10, 5)  # 5 numbers from 0 to 10
print(linspace)
#_____np.log() – Compute the natural logarithm of an array.
log=np.log(arr)
print(log)
#_____np.exp() – Compute the exponential of an array.
exp=np.exp(arr)
print(exp)