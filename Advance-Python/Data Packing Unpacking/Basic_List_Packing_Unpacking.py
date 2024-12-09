# -------------- List Packing -------------------

# List Packing: We pack multiple values into a list.
# It involves simply creating a list with multiple values, separated by commas.

# Example: Packing elements into a list
packed_list = [1, 2, 3, 4]
print("Packed List:", packed_list)
# Output: Packed List: [1, 2, 3, 4]

# Here, the values 1, 2, 3, and 4 are "packed" into a single list.

# Packing values of different types into a list:
mixed_packed_list = ["John", 25, True, 45.6]
print("Mixed Packed List:", mixed_packed_list)
# Output: Mixed Packed List: ['John', 25, True, 45.6]

# Here, the values of different types (string, integer, boolean, float) are packed into a list.


# -------------- List Unpacking -------------------

# List Unpacking: We extract values from a list and assign them to variables.
# Unpacking a list allows us to assign each element to a separate variable.

# Example: Unpacking elements from a list
unpacked_list = [1, 2, 3]
a, b, c = unpacked_list  # Unpacking the values into variables a, b, c
print(f"Unpacked Values: a = {a}, b = {b}, c = {c}")
# Output: Unpacked Values: a = 1, b = 2, c = 3

# Here, we unpack the list [1, 2, 3] into individual variables a, b, and c.

# If the number of variables doesn't match the list, Python raises a ValueError:
# unpacking_error = [1, 2]
# a, b, c = unpacking_error  # This would raise an error: ValueError: not enough values to unpack


# -------------- List Unpacking with * (Wildcard) -------------------

# The * (asterisk) operator allows us to unpack a portion of the list into a new list.
# This is useful when we don't know how many values are in the list, and we want to grab the rest of the elements.

# Example: Unpacking with * (Wildcard)
list_with_wildcard = [1, 2, 3, 4, 5]
first, *middle, last = list_with_wildcard
print(f"First: {first}, Middle: {middle}, Last: {last}")
# Output: First: 1, Middle: [2, 3, 4], Last: 5

# Here, the first and last elements are unpacked into separate variables.
# The remaining elements (2, 3, 4) are captured into the 'middle' list.


# -------------- Nested List Packing and Unpacking -------------------

# List packing and unpacking can also be performed on nested lists (lists within lists).

# Example: Nested List Packing
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested Packed List:", nested_list)
# Output: Nested Packed List: [[1, 2], [3, 4], [5, 6]]

# Example: Nested List Unpacking
nested_unpacking = [[1, 2], [3, 4], [5, 6]]
(a, b), (c, d), (e, f) = nested_unpacking  # Unpacking inner lists into individual variables
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")
# Output: a = 1, b = 2, c = 3, d = 4, e = 5, f = 6

# Here, we unpack each sub-list within the nested list into separate variables.
# The first sub-list [1, 2] is unpacked into a and b, the second into c and d, and the third into e and f.


# -------------- List Unpacking with * (Wildcard) in Nested Lists -------------------

# Just like with non-nested lists, the * operator can also be used in nested lists to capture multiple elements.

# Example: Unpacking with * (Wildcard) in a Nested List
nested_with_wildcard = [[1, 2], [3, 4], [5, 6], [7, 8]]
(first, *middle, last) = nested_with_wildcard
print(f"First: {first}, Middle: {middle}, Last: {last}")
# Output: First: [1, 2], Middle: [[3, 4], [5, 6]], Last: [7, 8]

# Here, we unpack the first and last nested lists and place the middle nested lists into a 'middle' list.


# -------------- Packing and Unpacking with List Methods -------------------

# We can also pack and unpack lists using built-in Python methods.

# Example: Packing a List using list() method
range_list = list(range(5))  # Creates a list of numbers from 0 to 4
print("Range List:", range_list)
# Output: Range List: [0, 1, 2, 3, 4]

# Example: Unpacking a List using list slicing
first_two = range_list[:2]
print("First Two Elements:", first_two)
# Output: First Two Elements: [0, 1]

# Here, we used slicing to unpack the first two elements from the list `range_list`.


# -------------- Conclusion -------------------

# List packing and unpacking are powerful features in Python that allow us to group and extract data efficiently.
# They help simplify the code, improve readability, and make it easier to work with multiple variables or values at once.

# With the * operator and list slicing, we can easily manage and manipulate large datasets in a flexible manner.
