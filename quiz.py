import numpy as np
import pandas as pd
import statistics as st
import random


# number 1

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print("Answer - ", c)

# ans [5,7,9]


# number 2

arr = np.array([0 for i in range(10)])

new_arr = arr.reshape(2,5)
print(new_arr)


# number 3

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data = np.array(data)

mean = data.mean()

median = np.median(data)

mode = st.mode(data.flatten())

standard_dev = np.std(data)

print("Mean - ", mean, " Mode - ", mode, " median - ", median, " standrad deviation - ", standard_dev)


# number 4

arr = np.array([i for i in random.sample(range(6), 6)])
print("Maximum value - ", max(arr), " Minimum value - ", min(arr))


# number 5

this_arr = np.array([[[0 for k in range(3)] for j in range(3)] for i in range(3)])

new_arr = this_arr.reshape(2)

print(new_arr)


# number 6

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)
data.flatten()

print(data.shape)