def genarator(x):
    for i in range(x):
        yield i**3

value=genarator(100)

for i in range(50):
    print(next(value))







