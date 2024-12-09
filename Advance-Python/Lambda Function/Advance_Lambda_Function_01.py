'''
Problem: Employee Management System
Scenario:
You are working as a software developer at a Human Resources (HR) firm.
Your task is to design a system that can perform CRUD (Create, Read, Update, and Delete) operations on employee records.
Each employee record contains information such as the employee's ID, name, age, department, and salary.

Your goal is to use lambda expressions, walrus operators, and perform CRUD operations on a nested dataset representing employees.
Additionally, you will need to filter, update, and delete employee records based on certain conditions.

Task:
Create: Add a new employee to the dataset.
Read: Get the details of an employee by their ID.
Update: Modify an employee’s details, such as their salary or department.
Delete: Remove an employee record by their ID.

Requirements:
Use lambda expressions to filter, sort, or update the dataset.
Use the walrus operator (:=) where appropriate to avoid repetitive calculations.
Perform CRUD operations (Create, Read, Update, Delete).
Use nested data structures (list of dictionaries).


Explanation:

Create Operation:
The create_employee function takes a dictionary as input and appends it to the employees list, adding a new employee record.

Read Operation:
The read_employee function uses a lambda expression inside the next() function to find and return the first employee with the specified ID.

Update Operation:
The update_employee function looks for the employee by ID and then updates the specified fields (like salary or department) using the **updates syntax to allow multiple fields to be updated at once.

Delete Operation:
The delete_employee function filters out the employee with the given ID by using a list comprehension, effectively removing that employee from the employees list.

Filter Operation:
The filter_high_salary lambda expression is used to filter employees based on their salary being greater than 60,000. The filter() function is used along with the lambda expression to perform the filtering.

Sort Operation:
The sort_by_age lambda expression sorts employees by their age using the sorted() function and a lambda as the sorting key.

Adjust Salary Operation:
The adjust_salary function checks if an employee’s salary is below a given threshold. If so, it uses the walrus operator (:=) to update the salary and print a confirmation message.



Here are the function names based on the naming conventions provided:

Create Function: create_employee
Read Function: read_employee
Update Function: update_employee
Delete Function: delete_employee
Filter Function (e.g., salary > 60000): filter_high_salary
Sort Function (e.g., sort by age): sort_by_age
Adjust Salary Function: adjust_salary
'''


employees = [
    {"id": 101, "name": "Alice", "age": 30, "department": "HR", "salary": 55000},
    {"id": 102, "name": "Bob", "age": 40, "department": "IT", "salary": 75000},
    {"id": 103, "name": "Charlie", "age": 35, "department": "Sales", "salary": 60000},
    {"id": 104, "name": "David", "age": 28, "department": "Marketing", "salary": 50000},
    {"id": 105, "name": "Eva", "age": 45, "department": "Finance", "salary": 90000},
]


# Read Function
read_employee = lambda id: [data for data in filter(lambda io:io['id']==id,employees) ]

print(f"\033[33mRead 103:\033[39m {read_employee(103)}")
print("\n\n")
# Update Function
update_employee = lambda id=None,name=None,age=None,department=None,salary=None: [
    {**employee,
     
     # Update name,age,dept,salary
     **({"name":name} if (name is not None and isinstance(name,str)) else {}),
     **({"age":age} if (age is not None and isinstance(age,int)) else {}),
     **({"department":department} if (department is not None and isinstance(department,str)) else {}),
     **({"salary":salary} if (salary is not None and isinstance(salary,int)) else {}),
     

    } if employee['id'] == id else employee
    for employee in employees
]

employees = update_employee(103,'Priyesh',23,'AIDS',100000)
print(f"\033[33mUpdated 103:\033[39m: {employees}")
print("\n\n")

# Create Function 
create_employee = lambda name,age,department,salary,employees: employees+[
    {
        **({"id": employees[-1]["id"] + 1} if employees else {"id": 1}),
        **({"name":name} if isinstance(name,str) else {}),
        **({"age":age} if isinstance(age,int) else {}),
        **({"department":department} if isinstance(department,str) else {}),
        **({"salary":salary} if isinstance(salary,int) else {}),
    }
    # for employee in employees
]

employees = create_employee('Ankur',23,'Mechanical',70000,employees)
print(f"\033[33mCreated 106:\033[39m {employees}")
print("\n\n")

# Delete Function
delete_employees = lambda id: [ data for data in filter(lambda io: io["id"]!=id,employees) ]

print(f"\033[33mDeleted 106:\033[39m {delete_employees(106)}")
print("\n\n")