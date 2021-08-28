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
import math

N = get_number()
M = get_number()
K=get_number()

def split(word):
    return [char for char in word]
mat=numpy.array([split(input()) for i in range(N)])

def special_points():
    return (get_number(),get_number())





def calculate_dis(x,y):
    x_dis = 0
    y_dis = 0
    pi = 0
    pj = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j]=="." and not(j in y) and not(i in x) :
                pi=i
                pj=j
            else:
                break

        x_dis=x_dis+pi
        y_dis=y_dis+pj
    return x_dis,y_dis

cal=calculate_dis(x[0],y[0])
print(cal)












x,y=get_number(),get_number()
calculate_dis(x,y)






