# Problem 3: Filtering Complex Data with Multiple Conditions
# You are developing a shipping system where each order consists of a user ID, delivery address,
# items ordered (in the form of tuples), and the status of the order. Your task is to filter orders where:

# The order is shipped.
# The total weight of the items is greater than 10 kg.
# The total number of items is more than 3.

orders = [
    {"order_id": 1, "user_id": 101, "status": "shipped","items": [("laptop", 2), ("phone", 1)], "address": "Address1","weight":7},
    {"order_id": 2, "user_id": 102, "status": "processing", "items": [("tv", 5), ("remote", 0.2)], "address": "Address2","weight":35},
    {"order_id": 3, "user_id": 103, "status": "shipped", "items": [("washing machine", 7), ("detergent", 0.5)], "address": "Address3","weight":90},
    {"order_id": 4, "user_id": 104, "status": "shipped", "items": [("air conditioner", 15), ("filter", 1)], "address": "Address4","weight":4}
] # [("laptop", 2), ("phone", 1)], means 2 laptops and 1 phone

# Task: Filter orders that are shipped, weigh more than 10 kg, and contain more than 3 items

filter_order_details = [
    print(order) for order in filter(lambda io: sum([quant[1] for quant in io["items"]])>3 and io['status']=="shipped" and io["weight"]>10,orders)
    
]
# print(filter_order_details)