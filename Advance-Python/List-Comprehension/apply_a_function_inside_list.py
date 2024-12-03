# Problem 4: Apply a function to every item in a list
# Problem: Given a list of strings, convert each string to uppercase.

words = ['hello', 'world', 'python']

uppercase = list(word.upper() for word in words)
print(f"Function applied: {uppercase}")