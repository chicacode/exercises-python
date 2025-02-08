import numpy as np

# Numpy class

# 1D
l1 = [3,6,9]

# 2D List: Is store data like a table
l2 = [[1,2,3], [4,5,6]]

print(l2[0][1]) # 2
print(l2[1][2]) # 6

# 2 Dimensions Numpy Arrays

np_2d = np.array([[70.2, 50.7, 46.9, 80.3, 67.8,  67.9], [30.2, 10.7, 66.9, 83.3, 17.8,  90.9]])

print('Shape: ', np_2d.shape)

np_2d[0,2]

# NumPy

print('average: ', np_2d.mean())

# Compute median array
median_arr = np.median(np_2d)
print('median: ', median_arr)
