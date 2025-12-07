import test_numpy as np
arr = np.array([1,2,3])
print(arr)

# check dimensions
arr0 = np.array(43)
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)

# shape of the array
arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr_2d.shape)

# datatype
print(arr_2d.dtype)

# adding two array
arr_a = np.array([1,2,3])
arr_b = np.array([4,5,6])
arr_c = np.concatenate((arr_a,arr_b))
print(arr_c)

# reshaping array
arr = np.arange(1,9)
reshaped = arr.reshape(2,4)
print(reshaped)

# Flattening Arrays
flat = reshaped.flatten()
print(flat)

# axis parameter
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
sum_row = np.sum(arr2d, axis=1)
sum_col = np.sum(arr2d, axis=0)
print(sum_row, sum_col)

# random module
from test_numpy import random
z = random.randint(100,size=10)
print(z)

# universal func
arr = np.array([1, 2, 3, 4])
sqrt_arr = np.sqrt(arr)
log_arr = np.log(arr)
print(sqrt_arr, log_arr)
