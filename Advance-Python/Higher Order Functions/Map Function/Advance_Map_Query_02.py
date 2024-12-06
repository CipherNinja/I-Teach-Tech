# Problem 2: Capitalizing Customer Names
# You are working on a customer management system, and the names of customers
# need to be capitalized before they are displayed on the front-end.

# Task: Use map() to capitalize all customer names.

customers = [
    {"customer_id": 1, "name": "john doe", "email": "john@example.com"},
    {"customer_id": 2, "name": "alice smith", "email": "alice@example.com"},
    {"customer_id": 3, "name": "bob johnson", "email": "bob@example.com"},
]

update_customer_names = [print(names) for names in map(lambda n: n['name'].upper(),customers)]