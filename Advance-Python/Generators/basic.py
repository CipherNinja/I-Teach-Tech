def even_generator(n):
    for i in range(n+1):
        yield i

def my_iterator():
    yield 1
    yield 2
    yield 3
gen = my_iterator()
print(next(gen))
print(next(gen))
print(next(gen))
# for y in even_generator(10):
#     print(y)