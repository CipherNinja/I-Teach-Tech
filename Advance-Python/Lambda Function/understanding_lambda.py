def _lambda_(x):
    x *= x
    return x

print(_lambda_(9)) # Output 81

# using lambda (anonymous function)
function = lambda x: x**2
print(function(2))