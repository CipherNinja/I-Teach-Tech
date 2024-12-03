# Problem 1: Create a Dictionary of Even Numbers and Their Squares
# Problem: Given a list of numbers, create a dictionary where the key is the number, and the value is its square, but only for even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

answer = {num:num**2 for num in numbers if num % 2==0}
print(answer)