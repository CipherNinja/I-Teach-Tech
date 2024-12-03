# The reduce() function from the functools module applies a binary function (a function with two arguments) cumulatively to the items in an iterable, so as to reduce the iterable to a single value.

# reduce(function,iterable)

from functools import reduce
number = [1,2,3,4,5]
reduced = reduce(lambda x,y:x+y,number)
# print(reduced)

# Problem: Using reduce with lambda, and list comprehension inside lambda to square even numbers


numbers = [x for x in range(1,11)]

reduced = reduce(lambda _variable_unused_,_unused_variable: sum([y**2 for y in numbers if y%2==0]),numbers)
print(reduced)

print(f"sum = {reduce(lambda _,__:sum([y**2 for y in numbers if y%2 ==0]),numbers)}")