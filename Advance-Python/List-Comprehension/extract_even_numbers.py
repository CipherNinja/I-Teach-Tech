# Problem 2: Extracting even numbers from a list
# Problem: Given a list of numbers, extract all the even numbers into a new list.


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Even Numbers: {[num for num in numbers if num%2 == 0]}")

# APPROACH [item for item in iterable if condition] 
