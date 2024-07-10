
# ==================================================
# There are three ways to practice arrays in python:
#        --~ Basic array operations ~--
# ==================================================

""" using list """

# Creating an array (list)
arr = [1, 2, 3, 4, 5]

# Accessing elements
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3

# Modifying elements
arr[1] = 7
print(arr)  # Output: [1, 7, 3, 4, 5]

# Adding elements
arr.append(6)
print(arr)  # Output: [1, 7, 3, 4, 5, 6]

# Removing elements
arr.remove(3)
print(arr)  # Output: [1, 7, 4, 5, 6]

# Iterating through the array
for i in arr:
    print(i)

""" using array module """

import array as array

# Creating an array of integers
a = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(a[0])  # Output: 1
print(a[2])  # Output: 3

# Modifying elements
a[1] = 7
print(a)  # Output: array('i', [1, 7, 3, 4, 5])

# Adding elements
a.append(6)
print(a)  # Output: array('i', [1, 7, 3, 4, 5, 6])

# Removing elements
a.remove(3)
print(a)  # Output: array('i', [1, 7, 4, 5, 6])

# Iterating through the array
for i in a:
    print(i)

""" using NumPy arrays """

import numpy as np

# Creating an array
ar = np.array([1, 2, 3, 4, 5])

# Accessing elements
print(ar[0])  # Output: 1
print(ar[2])  # Output: 3

# Modifying elements
ar[1] = 7
print(ar)  # Output: [1 7 3 4 5]

# Adding elements (Note: NumPy arrays have a fixed size, so you need to create a new array)
ar = np.append(ar, 6)
print(ar)  # Output: [1 7 3 4 5 6]

# Removing elements (Note: NumPy arrays have a fixed size, so you need to create a new array)
ar = np.delete(ar, 2)  # Removes element at index 2
print(ar)  # Output: [1 7 4 5 6]

# Iterating through the array
for i in ar:
    print(i)