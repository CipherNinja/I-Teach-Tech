# Problem: Define a function that checks if a number is even
# filter(function,iterable)

numbers = [1,2,3,4,5,6,7]
filter_out_even = list(filter(lambda x:x%2==0,numbers))
print(filter_out_even)