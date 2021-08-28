# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
def split(word):
    return [char for char in word]
N = get_number()
arr=numpy.array([])
x=numpy.array([])
for i in range(N):
    arr=split(numpy.append(arr,get_word()))

    x=numpy.append(x,sorted(split(arr[0]))[0])
    x=sorted(x)
    arr.pop()

print(''.join(str(i) for i in x))







