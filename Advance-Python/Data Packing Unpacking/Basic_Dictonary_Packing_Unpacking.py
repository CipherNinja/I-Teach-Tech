# -------------- Dictionary Packing -------------------

# Dictionary Packing: We "pack" key-value pairs into a dictionary.
# It's simply creating a dictionary with multiple key-value pairs.

# Example: Packing elements into a dictionary
packed_dict = {"id": 101, "name": "Alice", "age": 30, "department": "HR", "salary": 55000}
print("Packed Dictionary:", packed_dict)
# Output: Packed Dictionary: {'id': 101, 'name': 'Alice', 'age': 30, 'department': 'HR', 'salary': 55000}

# Here, the key-value pairs represent an employee's details: 'id' is the key, and 101 is the value.

# Packing with dynamic values
new_employee = {"id": 106, "name": "Ankur", "age": 23, "department": "Mechanical", "salary": 70000}
print("New Employee Packed:", new_employee)
# Output: New Employee Packed: {'id': 106, 'name': 'Ankur', 'age': 23, 'department': 'Mechanical', 'salary': 70000}


# -------------- Dictionary Unpacking -------------------

# Dictionary Unpacking: We extract values from a dictionary and assign them to variables.
# This is similar to list unpacking, but instead of indexing, we extract the keys.

# Example: Unpacking elements from a dictionary
employee = {"id": 101, "name": "Alice", "age": 30, "department": "HR", "salary": 55000}

# Here, we unpack the dictionary into variables corresponding to the keys.


# -------------- CRUD Operations on Dictionary -------------------

# CRUD Operations (Create, Read, Update, Delete) are the basic operations you can perform on a dataset like a dictionary.

# Sample Employee Data
employees = [
    {"id": 101, "name": "Alice", "age": 30, "department": "HR", "salary": 55000},
    {"id": 102, "name": "Bob", "age": 40, "department": "IT", "salary": 75000},
    {"id": 103, "name": "Charlie", "age": 35, "department": "Sales", "salary": 60000},
    {"id": 104, "name": "David", "age": 28, "department": "Marketing", "salary": 50000},
    {"id": 105, "name": "Eva", "age": 45, "department": "Finance", "salary": 90000},
]

# --------------------- CREATE ---------------------
# The `create_employee` function adds a new employee to the dataset.
# It will "pack" the new employee data into a dictionary and append it to the list.

def create_employee(id, name, age, department, salary):
    new_employee = {"id": id, "name": name, "age": age, "department": department, "salary": salary}
    employees.append(new_employee)
    return new_employee

new_employee = create_employee(106, "Ankur", 23, "Mechanical", 70000)
print(f"Created Employee: {new_employee}")
# Output: Created Employee: {'id': 106, 'name': 'Ankur', 'age': 23, 'department': 'Mechanical', 'salary': 70000}

# --------------------- READ ---------------------
# The `read_employee` function retrieves an employee's data by their `id`.
# It "unpacks" the dictionary values and returns the employee details.

def read_employee(id):
    return next((emp for emp in employees if emp["id"] == id), None)

employee = read_employee(103)
print(f"Read Employee with ID 103: {employee}")
# Output: Read Employee with ID 103: {'id': 103, 'name': 'Charlie', 'age': 35, 'department': 'Sales', 'salary': 60000}

# --------------------- UPDATE ---------------------
# The `update_employee` function allows modifying the employee's details based on their ID.
# It "unpacks" the dictionary and updates the required fields.

def update_employee(id, name=None, age=None, department=None, salary=None):
    employee = next((emp for emp in employees if emp["id"] == id), None)
    if employee:
        # Update values based on the provided arguments
        if name: employee["name"] = name
        if age: employee["age"] = age
        if department: employee["department"] = department
        if salary: employee["salary"] = salary
    return employee

updated_employee = update_employee(104, name="David Smith", salary=52000)
print(f"Updated Employee: {updated_employee}")
# Output: Updated Employee: {'id': 104, 'name': 'David Smith', 'age': 28, 'department': 'Marketing', 'salary': 52000}

# --------------------- DELETE ---------------------
# The `delete_employee` function removes an employee's data from the dataset by their `id`.
# It "unpacks" the list and filters out the employee to delete.

def delete_employee(id):
    global employees
    employees = [emp for emp in employees if emp["id"] != id]
    return employees

deleted_employees = delete_employee(106)  # Deleting the employee with ID 106 (Ankur)
print(f"Employees after Deletion: {deleted_employees}")
# Output: Employees after Deletion: [{'id': 101, 'name': 'Alice', 'age': 30, 'department': 'HR', 'salary': 55000}, ...]

# --------------------- Filter ---------------------
# The `filter_high_salary` function filters employees who have a salary greater than a given threshold.

def filter_high_salary(threshold):
    return [emp for emp in employees if emp["salary"] > threshold]

high_salary_employees = filter_high_salary(60000)
print(f"Employees with Salary > 60000: {high_salary_employees}")
# Output: Employees with Salary > 60000: [{'id': 102, 'name': 'Bob', 'age': 40, 'department': 'IT', 'salary': 75000}, ...]

# --------------------- Sort ---------------------
# The `sort_employees_by_age` function sorts employees based on their age.

def sort_employees_by_age():
    return sorted(employees, key=lambda emp: emp["age"])

sorted_employees = sort_employees_by_age()
print(f"Sorted Employees by Age: {sorted_employees}")
# Output: Sorted Employees by Age: [{'id': 104, 'name': 'David', 'age': 28, 'department': 'Marketing', 'salary': 50000}, ...]

# -------------- Conclusion ---------------------

# Dictionary packing and unpacking, along with CRUD operations, allow you to handle employee data dynamically.
# You can "pack" data into dictionaries, "unpack" values for processing, and perform CRUD operations like adding, updating, deleting, and reading employee records efficiently.

# This is useful in real-world projects for tasks such as managing HR data, inventory management, and customer data, where dictionary-based CRUD operations are common.
