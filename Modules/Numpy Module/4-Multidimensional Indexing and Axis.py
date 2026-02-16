import numpy as np

#  Axes in a 2D Array
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])



print(np.sum(arr, axis=0))  # Sum along rows (down each column)Operations move down the columns.
print(np.sum(arr, axis=1))  # Sum along columns (across each row)Operations move across the rows.

#2. Indexing in Multidimensional Arrays______

# Accessing an element
print(arr[1, 2])  # Row index 1, Column index 2 → Output: 6
print(arr[0:2, 1:3])  # Extracts first 2 rows and last 2 columns output=[2,3],[5,6]


#  Indexing in 3D Arrays
arr3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])

# Output of arr3D.shape is → (depth, rows, columns)
print(arr3D.shape)  # Output: (2, 2, 3) 

# First sheet, second row, third column
print(arr3D[0, 1, 2])  # Output: 6

print(arr3D[:, 0, :])   # Get the first row from both sheets

# 4. Practical Example: Selecting Data Along Axes

# Get all rows of the first column
first_col = arr[:, 0]
print(first_col)  # Output: [1 4 7]
# Get the first row from each "sheet" in a 3D array
first_rows = arr3D[:, 0, :]
print(first_rows)


# 5. Changing Data Along an Axis
# Replace all elements in column 1 with 0
arr[:, 1] = 0
print(arr)
