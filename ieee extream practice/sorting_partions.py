import math
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
n=get_number()
arr=numpy.array([],dtype='int32')
sub_arr=numpy.array([])
new=numpy.array([])
x=numpy.array([])

for _ in range(n):
    arr=numpy.append(arr,get_number())
print(arr)

for i in range(n):
    for j in range(n):
         sub_arr=numpy.append(sub_arr,arr[i:j])
         x=numpy.append(x,sub_arr)
    
    print(x)




