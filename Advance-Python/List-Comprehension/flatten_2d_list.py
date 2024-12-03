# Problem 3: Flatten a 2D List
# Problem: Given a 2D list (list of lists), flatten it into a single list containing all the elements.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Sublists: {[sublist for sublist in matrix]}")
print(f"Flatten List: {[item for sublist in matrix for item in sublist]}")
