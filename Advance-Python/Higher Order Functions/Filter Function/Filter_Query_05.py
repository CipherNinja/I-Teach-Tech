# Problem 6: Filtering by Tuple Length
# You are working with a list of tuples, where each tuple contains data about a product (name, price, quantity).
# Your task is to filter out products that have a quantity less than 5.
products = [
    ("Laptop", 50000, 2),
    ("Phone", 15000, 10),
    ("Headphones", 2500, 4),
    ("Monitor", 12000, 0)
]
# Task: Use filter() to get a list of products that have a quantity greater than or equal to 5.
filter_data = [(product,quantity) for (product,price,quantity) in filter(lambda prod:prod[2]<5,products)]
print(filter_data)

