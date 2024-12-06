# map(function, iterable)
# Problem: Map each elements of list and sqaure it

numbers = [1,2,3,4,5,6,7]
mapping = map(lambda x: x**2,numbers)
print(list(mapping))

# single line code 

print(f"single line code: {list(map(lambda x:x**2,[num for num in range(1,8)]))}")