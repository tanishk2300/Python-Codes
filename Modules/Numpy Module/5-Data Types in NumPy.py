import numpy as np 

arr=np.array([1,2,3,4,5])
print(arr.dtype)# Output: int64 (or int32 depending on the system.)

'''Common Data Types in NumPy:
int32, int64: Integer types with different bit sizes.
float32, float64: Floating-point types with different precision.
bool: Boolean data type.
complex64, complex128: Complex number types.
object: For storing objects (e.g., Python objects, strings).'''


#_____2. Changing Data Types__________

arr = np.array([1.5, 2.7, 3.9])
print(arr.dtype)  # Output: float64
arr_int = arr.astype(np.int32)  # Converting float to int
print(arr_int)    # Output: [1 2 3]
print(arr_int.dtype)  # Output: int32

arr_large = np.array([1000000, 2000000, 3000000], dtype=np.int64)
arr_small = arr_large.astype(np.int32)  # Downcasting to a smaller dtype
print(arr_small)  # Output: [1000000 2000000 3000000]
print(arr_small.dtype)  # Output: int32

#3. Why Data Types Matter in NumPy___________
arr_int64 = np.array([1, 2, 3], dtype=np.int64)
arr_int32 = np.array([1, 2, 3], dtype=np.int32)

print(arr_int64.nbytes)  # Output: 24 bytes (3 elements * 8 bytes each)
print(arr_int32.nbytes)  # Output: 12 bytes (3 elements * 4 bytes each)

#4. String Data Type in NumPy________________
arr = np.array(['apple', 'banana', 'cherry'], dtype='U10')  # Unicode string array
print(arr)

#5. Complex Numbers______
arr = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype='complex128')
print(arr)

#6. Object Data Type_______
arr = np.array([{'a': 1}, [1, 2, 3], 'hello'], dtype=object)
print(arr)