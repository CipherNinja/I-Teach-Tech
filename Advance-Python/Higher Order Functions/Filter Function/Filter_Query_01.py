# Problem 1: Employee Data Filtering
# You are a developer at XYZ Corporation, 
# and your task is to filter the employees who have a salary greater than ₹50,000 from
# the API response containing employee data in the form of a list of dictionaries.
# Task: Use filter() to get a list of employees with salaries greater than ₹50,000.
employees = [
    {"name": "John", "salary": 55000},
    {"name": "Alice", "salary": 45000},
    {"name": "Bob", "salary": 60000},
    {"name": "Mary", "salary": 48000}
]
limit=50000
filter_out_salary = [ data for data in filter(lambda x:x['salary']>limit,employees) ]
print(filter_out_salary)