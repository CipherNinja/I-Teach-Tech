# Packing multiple values into a tuple
packed_tuple = (1, 2, 3, 4)
print(packed_tuple)  # Output: (1, 2, 3, 4)

# Packing values into a tuple without parentheses
packed_tuple = 1, 2, 3, 4
print(packed_tuple)  # Output: (1, 2, 3, 4)

# Packing values into a tuple
packed_tuple = (1, 2, 3, 4)

# Unpacking tuple values into variables
a, b, c, d = packed_tuple
print(a, b, c, d)  # Output: 1 2 3 4

# Packing values into a tuple
packed_tuple = (1, 2, 3)

# Trying to unpack into fewer variables
# This will raise a ValueError
try:
    a, b = packed_tuple
except ValueError as v:
    print("a, b = packed_tuple || Causing Value Error")



# Packing values into a tuple
packed_tuple = (1, 2, 3, 4, 5)

# Unpacking with * to capture the middle values
first,*middle,last = packed_tuple
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5

# Packing values into a tuple
packed_tuple = (1, 2, 3, 4, 5)

# Unpacking with * to capture the first values
*first, last = packed_tuple
print(first)  # Output: [1, 2, 3, 4]
print(last)   # Output: 5


# Packing a nested tuple
nested_tuple = (1, (2, 3), (4, 5))

# Unpacking nested tuple
a, (b, c), (d, e) = nested_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5


# Define a function that takes a tuple as arguments
def process_employee_details(details):
    name, age, department = details
    print(f"Name: {name}, Age: {age}, Department: {department}")

# Packing values into a tuple
employee = ("Alice", 30, "HR")

# Unpacking the tuple when passing as an argument
process_employee_details(employee)
# Output: Name: Alice, Age: 30, Department: HR


# Packing a list of tuples
employee_data = [("Alice", 30, "HR"), ("Bob", 40, "IT"), ("Charlie", 35, "Sales")]

# Unpacking in a loop
for name, age, department in employee_data:
    print(f"Name: {name}, Age: {age}, Department: {department}")


# Packing and unpacking values
x, y, z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3


# Swapping values
x, y = 5, 10
x, y = y, x
print(x, y)  # Output: 10 5

# Packing a tuple
person = ("Alice", 30)

# Unpacking with a default value
name, age, department = person + ("Unknown",)  # Adding a default value
print(name, age, department)  # Output: Alice 30 Unknown


# Function that returns multiple values as a tuple
def get_employee_details():
    return "Alice", 30, "HR"

# Unpacking the returned tuple
name, age, department = get_employee_details()
print(name, age, department)  # Output: Alice 30 HR

