'''
Scenario 2: Retry Mechanism with Decorator
Problem:

You are working on a distributed system where API calls can sometimes fail due to network issues or server downtime. You need to implement a retry mechanism that attempts to call a function multiple times before failing completely.

Task:

Create a decorator retry_on_failure that will attempt to execute a function a specified number of times (e.g., 3 times) if it raises an exception. If the function continues to fail, it should return a failure message.

Requirements:

The decorator should accept a number max_retries as a parameter.
The decorator should catch exceptions raised by the function and retry the specified number of times.
If the function keeps failing, return a message like "Maximum retries reached. Request failed."
'''
import random

def retry_on_fail(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(F"ENDPOINT: {func.__name__}/{args}/{kwargs or None}")
            attempt = 0 
            while attempt < max_retries:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"{attempt+1} Attempt Failed")
                    attempt += 1
            if attempt > max_retries:
                print(f"Max Retries Exceeded {attempt}")


        return wrapper
    return decorator

# Use decorator in this given function
@retry_on_fail(max_retries=3)
def fetch_data_from_server(request_id):
    # Simulating a random failure
    if random.random() < 0.5:  # 50% chance to fail
        raise Exception("Network Error")
    return {"status": "success", "data": f"Data for request {request_id}"}

print(fetch_data_from_server(101))