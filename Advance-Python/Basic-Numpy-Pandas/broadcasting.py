import numpy as N

array = N.array(
    [
        [1,2,3,4,5],
        [2,3,4,5,6],
        [3,4,5,6,7],
        [4,5,6,7,8],
        [5,6,7,8,9],
    ]
)
# matrix multiplication
# print(array @ array.T)

array_2 = N.array([
    [2],[3],[4],[5],[6]
])

array_3 = array * array_2
print(array_3)