# Problem 2: Create a Dictionary of Squares
# Problem: Given a list of numbers, create a new dictionary where the key is the number and the value is its square.


# APPROACH {key_expression:value_expression for (key,value) in iterable}
dictonary = {item:item**2 for item in range(1,11)}
print(dictonary)