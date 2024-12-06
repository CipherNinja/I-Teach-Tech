# Problem 2: Multi-level Nested Tuple Filtering
# You are working on a data analysis tool that processes financial transactions.
# Each transaction is represented by a nested tuple, where the first element is a transaction ID,
# and the second element is a list of items purchased along with their prices.

transactions,budget_limit = [
    (1, [("apple", 20), ("banana", 10), ("orange", 15)]),
    (2, [("laptop", 500), ("mouse", 20)]),
    (3, [("notebook", 5), ("pen", 2), ("eraser", 1)]),
    (4, [("phone", 300), ("headphones", 50)]),
],100
# Your task is to filter out transactions where the total cost of items exceeds a specific budget limit.
x= transactions
exceeded_expences = [data for data in list(filter(lambda x:sum([meta[1] for meta in x[1]])>budget_limit,transactions))]
print(exceeded_expences)