# use decorators to say hello world and return the control back to the function itself in the end

def say_hello_world(func):
    def wrapper(*arg,**kwarg):
        print("Hello World from DECORATOR")
        control_to_table_function = func(*arg,**kwarg)
        return control_to_table_function
    return wrapper

# decorator for regular functions
@say_hello_world
def Table_Of_(number):
    return [table*number for table in range(1,11)]

print(f"Using Regular Function: {Table_Of_(2)}\n")



# Decorator for lambda functions
table_of_ = say_hello_world(lambda number: [table*number for table in range(1,11)])
print(f"Using Lamda Function: {table_of_(2)}")