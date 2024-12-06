# Project Overview:
# This project simulates a basic e-commerce cart system where a list of products is managed,
# allowing the application of discounts, filtering of out-of-stock items, and calculation of final prices,
# including VAT (Value Added Tax). The main focus of the project is to use Python's functional programming
# techniques such as map(), filter(), and reduce() for efficient and clean data processing.

"""
Project Title: E-Commerce Cart System with Discount and VAT Calculation

Key Features:
- Product Data Management: Handle product information like name, price, and stock.
- Out-of-Stock Filtering: Filter out products that are out of stock (stock == 0).
- Discount Application: Apply a 15% discount to each product.
- VAT Calculation: Calculate 15% VAT on the discounted price.
- Total Price Calculation: Calculate the final price including VAT.

Technical Details:
- Data Structures:
  - The products are represented as a list of dictionaries with attributes:
    - product_id: Unique identifier for the product.
    - name: Name of the product.
    - price: Original price before discount.
    - stock: Number of items available in stock.
- Functional Programming:
  - map(): Used to apply the discount to each product's price.
  - filter(): Filters out products with zero stock.
  - reduce(): Computes the total price and VAT by reducing the list of products.
- Mathematical Computations:
  - Discount: A 15% discount is applied to the original price.
  - VAT: A 15% VAT is applied to the final discounted price.

Steps Involved:
1. Filter out products with zero stock using filter().
2. Apply a 15% discount on each available product's price using map().
3. Use reduce() to calculate the total price of the discounted products.
4. Calculate the VAT (15%) on the total price and compute the final price.
5. Display the available products, discounted prices, and the final total price including VAT.

Example Code Implementation:
- The code applies the discount and VAT to a list of products using map(), filter(), and reduce().
- The final result prints the updated product information and the total price with VAT.

"""
products = [
    {'product_id': 1, 'name': 'Premium Fridge', 'price': 349.65, 'stock': 12, 'category': 'Home Appliances', 'rating': 4.2},
    {'product_id': 2, 'name': 'Wireless Chair', 'price': 80.91, 'stock': 58, 'category': 'Furniture', 'rating': 3.9},
    {'product_id': 3, 'name': 'Durable Sneakers', 'price': 45.30, 'stock': 35, 'category': 'Clothing', 'rating': 4.5},
    {'product_id': 4, 'name': 'Compact Microwave', 'price': 122.40, 'stock': 0, 'category': 'Home Appliances', 'rating': 3.7},
    {'product_id': 5, 'name': 'Smart Laptop', 'price': 599.99, 'stock': 25, 'category': 'Electronics', 'rating': 4.8},
    {'product_id': 6, 'name': 'Advanced Sofa', 'price': 399.45, 'stock': 7, 'category': 'Furniture', 'rating': 4.3},
    {'product_id': 7, 'name': 'Wireless TV', 'price': 299.99, 'stock': 50, 'category': 'Electronics', 'rating': 4.1},
    {'product_id': 8, 'name': 'Smartphone', 'price': 279.55, 'stock': 5, 'category': 'Electronics', 'rating': 4.6},
    {'product_id': 9, 'name': 'Portable Microwave', 'price': 99.99, 'stock': 30, 'category': 'Home Appliances', 'rating': 4.0},
    {'product_id': 10, 'name': 'Eco-friendly Sneakers', 'price': 60.45, 'stock': 10, 'category': 'Clothing', 'rating': 4.3},
    {'product_id': 11, 'name': 'Gaming Headset', 'price': 129.99, 'stock': 100, 'category': 'Electronics', 'rating': 4.7},
    {'product_id': 12, 'name': 'Smart Watch', 'price': 150.00, 'stock': 45, 'category': 'Electronics', 'rating': 4.3},
    {'product_id': 13, 'name': 'Electric Kettle', 'price': 35.50, 'stock': 80, 'category': 'Home Appliances', 'rating': 4.2},
    {'product_id': 14, 'name': 'Bluetooth Speaker', 'price': 79.99, 'stock': 15, 'category': 'Electronics', 'rating': 4.5},
    {'product_id': 15, 'name': 'Ergonomic Office Chair', 'price': 210.75, 'stock': 20, 'category': 'Furniture', 'rating': 4.6},
    {'product_id': 16, 'name': 'Washing Machine', 'price': 499.99, 'stock': 10, 'category': 'Home Appliances', 'rating': 4.0},
    {'product_id': 17, 'name': 'Portable Air Conditioner', 'price': 199.99, 'stock': 8, 'category': 'Home Appliances', 'rating': 3.8},
    {'product_id': 18, 'name': 'Stainless Steel Toaster', 'price': 50.00, 'stock': 15, 'category': 'Home Appliances', 'rating': 4.1},
    {'product_id': 19, 'name': 'Leather Jacket', 'price': 249.99, 'stock': 25, 'category': 'Clothing', 'rating': 4.7},
    {'product_id': 20, 'name': 'Electric Fan', 'price': 25.50, 'stock': 40, 'category': 'Home Appliances', 'rating': 3.5},
    {'product_id': 21, 'name': 'Cordless Vacuum Cleaner', 'price': 159.00, 'stock': 50, 'category': 'Home Appliances', 'rating': 4.4},
    {'product_id': 22, 'name': 'Yoga Mat', 'price': 18.95, 'stock': 30, 'category': 'Sports', 'rating': 4.3},
    {'product_id': 23, 'name': 'Sports Shoes', 'price': 85.90, 'stock': 60, 'category': 'Clothing', 'rating': 4.0},
    {'product_id': 24, 'name': 'Camera Lens', 'price': 399.00, 'stock': 12, 'category': 'Electronics', 'rating': 4.5},
    {'product_id': 25, 'name': 'Car Seat Cover', 'price': 49.99, 'stock': 35, 'category': 'Automotive', 'rating': 4.0},
    {'product_id': 26, 'name': 'Backpack', 'price': 29.99, 'stock': 70, 'category': 'Clothing', 'rating': 4.2},
    {'product_id': 27, 'name': 'Waterproof Boots', 'price': 95.00, 'stock': 18, 'category': 'Clothing', 'rating': 4.6},
    {'product_id': 28, 'name': 'LED Desk Lamp', 'price': 35.00, 'stock': 55, 'category': 'Furniture', 'rating': 4.1},
    {'product_id': 29, 'name': 'Smart Refrigerator', 'price': 799.99, 'stock': 3, 'category': 'Home Appliances', 'rating': 4.8},
    {'product_id': 30, 'name': 'Portable Power Bank', 'price': 25.99, 'stock': 100, 'category': 'Electronics', 'rating': 4.4}
]



filter_out_zero_stock = [goodies for goodies in filter(lambda items: items['stock'] > 0,products)]
apply_discount = [{**goodies, "price":round(goodies['price'] - (goodies['price']*0.15),3)} for goodies in filter_out_zero_stock]
# print(apply_discount)

# EASY APPROACH
discounted = [goodies for goodies in map(lambda item:round(item['price'] - (item['price']*0.15),3),filter_out_zero_stock)]
# total_discounted_price = sum(discounted_price)
# print(round(total_discounted_price,3))
from functools import reduce
total_discounted_price = reduce(lambda acc,_:round(sum(discounted),3) ,apply_discount)

# Display the available products and their discounted prices
for product in apply_discount:
    print(f"{product['name']} | Discounted Price: ₹{product['price']} |")

total_discounted_price = f"\n\nTotal Discounted Price: {total_discounted_price}\nVAT (15%): {total_discounted_price*0.15}\nActual Price: {round(total_discounted_price-total_discounted_price*0.15,3)}"
print(total_discounted_price)

