# Problem 3: Create a Dictionary with Filtered Items (Using filter())
# Problem: Given a list of mixed integers (both positive and negative), create a dictionary where the key is the number, and the value is the number squared, but only for positive numbers.

numbers = [-1, -2, 3, 4, -5, 6]
filtered_dict_of_sqaured_positive_number = {number:number**2 for number in list(filter(lambda x: x>0,numbers))} # list() is optional
print(filtered_dict_of_sqaured_positive_number)