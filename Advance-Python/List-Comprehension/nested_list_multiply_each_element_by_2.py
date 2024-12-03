# Problem 5: Nested List Comprehensions for Matrix Operations
# Problem: Multiply each element in a 2D matrix by 2.

matrix = [[1, 2], [3, 4], [5, 6]]

multiplied_2d = [[element*2 for element in sublist] for sublist in matrix]
print(multiplied_2d)

multiplied_plus_flatten = [element*2 for sublist in matrix for element in sublist]
print(multiplied_plus_flatten)