import numpy as np
import pandas as pd

# check out the current version
# print(np.__version__)

# starting from here
my_list = [1,2,3,4]
my_list = my_list * 2
# print(my_list)

# np 

array = np.array([1,2,3,4])
# print(array)
# print(type(array))

# double the elements in array

array = array * 2
# print(array)

# MULTIDIMENSIONAL ARRAY

# zero dimensional array
z = np.array('a')
# print(z)
# print(z.ndim)

# two dimensional array

two_dim = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
]


three_dim = [
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['1','2','3'],['4','5','6'],['7','8','9']],
    [['11','12','13'],['14','15','16'],['17','18','19']],
]

three_d_array = np.array(three_dim)
# print(three_d_array.shape)

# print(three_d_array[1,0,-1])

array = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
)

# array[start:end:step]
# print(array[0])
# print(array[0:3])
# print(array[0:3:2])
# print(array[::-1])

# column selection
# print(array[:,2])

# select the column for [all_rows, start:end]
# print(array[:,0:3])
print(array[0:2,1:3])
