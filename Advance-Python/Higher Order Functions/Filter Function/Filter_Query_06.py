# Problem 7: Filtering Strings by Length
# You are tasked with processing a list of names returned by a user input form.
# You need to filter out names that are longer than 6 characters.

names = ["John", "Alice", "Bob", "Michael", "Mary", "Sam"]
# Task: Use filter() to return a list of names that have a length of 6 or fewer characters.

filter_name = [ name for name in filter(lambda x: len(x)<=6,names)]
print(filter_name)

# or
print(f'{[ name for name in filter(lambda x: len(x)<=6,["John", "Alice", "Bob", "Michael", "Mary", "Sam"])]}')