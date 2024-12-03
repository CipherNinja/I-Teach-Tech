# Problem 1: Create a list of squares
# Problem: Given a list of numbers, create a new list containing the square of each number.

numbers = [1, 2, 3, 4, 5]
# APPROACH  [item for item in iterable]

SQ = [item**2 for item in numbers] # here number is an iterable data structure
print(SQ) # output : [1, 4, 9, 16, 25]

"For more comprehensive style you can Write the complete code in single line"

print(f"This will also print the same result: {[item**2 for item in range(1,6)]}")
