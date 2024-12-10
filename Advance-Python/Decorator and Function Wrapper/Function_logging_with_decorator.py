'''
Scenario 1: Logging Decorator for API Requests
Problem:

You are working on a web API where multiple API endpoints are defined. As part of the debugging and performance analysis process, you need to log the execution time and other details (like the endpoint name and the arguments passed) for each API request.

Task:

Create a logging decorator that will log the execution time, arguments, and the name of the function for every API call. You can assume the API calls are just function calls for now.

Requirements:

The decorator should log the function name.
It should log the arguments passed to the function.
It should log the time taken for the function to execute.
It should print the log in a human-readable format.
'''

import time

# Logging Decorator
def log_api_request(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        print(f"API Endpoint: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        
        result = func(*args, **kwargs)  # Call the original function
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.4f} seconds")
        
        return result
    
    return wrapper

# Example API functions

@log_api_request
def get_user_info(user_id):
    time.sleep(2)  # Simulate a delay
    return {"user_id": user_id, "name": "John Doe"}

@log_api_request
def create_user(name, age):
    time.sleep(1)  # Simulate a delay
    return {"status": "success", "name": name, "age": age}

# Calling API endpoints
print(get_user_info(123))
print(create_user("Alice", 30))
