import numpy as np

weight = [70.2, 50.7, 46.9, 80.3, 67.8]
height = [1.69, 1.70, 1.40, 1.80, 1.50]

np_weight = np.array(weight)
np_height = np.array(height)

print('RESULT BMI:', np_weight / np_height ** 2)