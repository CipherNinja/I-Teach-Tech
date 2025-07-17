'''
Problem: Advanced Dataset Transformation with Decorators
Scenario: Employee Performance and Salary Analysis
You are a data engineer at a company tasked with analyzing employee performance and salary data.
The dataset contains employee details such as their name, department, age, salary, and performance score.
Your task is to write a set of functions that process this data using advanced Python techniques such as map(),
filter(), reduce(), and comprehensions.

However, the company wants to add extra functionality using decorators for logging, validation, and performance benchmarking.

Task:
Write a function analyze_employees that:

Filters out employees with a performance score below a certain threshold.
Calculates a 10% salary hike for employees who pass the threshold.
Returns a summary of employees including their names, updated salaries, and departments.
Use decorators to:

Log: Log the execution details (function name, arguments, and execution time).
Validate: Ensure that the input dataset is a list of dictionaries and that required keys exist.
Benchmark: Measure the time taken for execution.
Requirements:
Use map(), filter(), and list comprehensions inside the function to perform the transformations.
Use Python’s advanced decorator features (like closures and nested decorators) to implement the decorators.

EXPECTED OUTPUT:
[LOG] Function: analyze_employees
[LOG] Arguments: [{'name': 'Alice', 'department': 'HR', 'age': 30, 'salary': 50000, 'performance': 85}, {...}], performance_threshold=80
[LOG] Result: [{'name': 'Alice', 'department': 'HR', 'updated_salary': 55000.0}, ...]

Execution Time: 0.0012 seconds
[{'name': 'Alice', 'department': 'HR', 'updated_salary': 55000.0}, {'name': 'Charlie', 'department': 'Finance', 'updated_salary': 66000.0}, {'name': 'Eva', 'department': 'Sales', 'updated_salary': 88000.0}]

'''


import time
from functools import reduce

# Sample Dataset
employees = [
    {"name": "Alice", "department": "HR", "age": 30, "salary": 50000, "performance": 85},
    {"name": "Bob", "department": "IT", "age": 40, "salary": 75000, "performance": 65},
    {"name": "Charlie", "department": "Finance", "age": 35, "salary": 60000, "performance": 90},
    {"name": "David", "department": "Marketing", "age": 28, "salary": 45000, "performance": 55},
    {"name": "Eva", "department": "Sales", "age": 45, "salary": 80000, "performance": 92},
]


def logging_function(func):
    def wrapper(*arg,**kwarg):
        start = time.time()
        key_value = {
            key:f"{key} = {value}" for key,value in kwarg.items()
        }
        print(f"[LOG] Function: {func.__name__}")
        print(f"[LOG] Arguments: {arg,key_value['performance_threshold']}")
        control = func(*arg,**kwarg)
        end = time.time()
        execution_time = end - start
        print(f"Execution Time: {execution_time:.4f}")
        return control
    return wrapper

# Step 1: Create a function to analyze employees
@logging_function
def analyze_employees(data, performance_threshold):
    """
    Filters employees based on performance, applies a 10% salary hike, and returns a summary.
    based on performance threshold
    """
    # Filter employees based on performance threshold
    filtered_employees = filter(lambda emp: emp["performance"] >= performance_threshold, data)
    
    # Apply a 10% salary hike using map()
    updated_employees = map(
        lambda emp: {
            **emp,
            "salary": round(emp["salary"] * 1.10, 2),  # 10% hike
        },
        filtered_employees
    )
    
    # Create a summary with list comprehension
    summary = [
        {"name": emp["name"], "department": emp["department"], "updated_salary": emp["salary"]}
        for emp in updated_employees
    ]
    
    return summary

# Call the function
print(analyze_employees(employees, performance_threshold=80))

'''
NOTE:
    1. Above code is given and you have to work on decorator part to fullfil your task
'''

