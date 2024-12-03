# Problem 5: Count the Occurrences of Each Product in an Order
# Problem: Given a list of product names that a customer has ordered,
# create a dictionary where the key is the product name, and the value is the count of how many times that product was ordered.

order = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

count_product_in_order = {
    product:order.count(product) for product in order
}
print(count_product_in_order)