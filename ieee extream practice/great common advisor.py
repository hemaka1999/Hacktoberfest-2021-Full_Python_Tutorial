# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


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


A = get_number()
B = get_number()
D = 1
n = 1
x = numpy.array([])
while n <=A and n <= B:
    if A % n == 0 and B % n == 0:
        to_append=numpy.array([n])
        x=numpy.append(x,to_append)
    n += 1

print(int(max(x)))



