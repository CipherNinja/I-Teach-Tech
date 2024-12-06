# Problem 5: Filtering Mixed Data Structures
# You are handling a large dataset consisting of multiple data types such as lists, tuples, and dictionaries. Your goal is to filter out elements from a list that are:

# Non-numeric values (including dictionaries and strings).
# Tuples with fewer than 3 elements.

mixed_data = [
    {"name": "John", "age": 30},
    (1, 2),
    10,
    "hello",
    (3, 4, 5),
    50,
    {"city": "New York"},
    (6, 7, 8),
    "world",
]

# Task: Filter non-numeric values and tuples with fewer than 3 elements

filter_mixed_data = [
    print(data,end="\n") for data in filter(
        lambda datatype:isinstance(datatype,(int,float)) or (isinstance(datatype,tuple) and len(datatype)<3),
        mixed_data)
]