# Problem 8: Filter Products Based on Price Range
# Problem: You have a dictionary of products with their prices.
# Create a new dictionary that includes only the products that are within a specified price range.

products = {
    'laptop': 1500,
    'phone': 700,
    'headphones': 100,
    'tablet': 300
}
# Price range filter
min_price = 100
max_price = 1000

filter_product = {
    product:price for (product,price) in products.items() if (price >= min_price and price <= max_price) 
}
print(filter_product)