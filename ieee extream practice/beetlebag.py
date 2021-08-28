# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) >=1:
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



n=0
test_cases  = get_number()

for j in range(test_cases):
    power = numpy.array([0])
    gadget_weight = 0
    capacity = get_number()
    n=get_number()
    for i in range(n):
        current_weight=get_number()
        current_power=get_number()
        if current_weight<=capacity:
            for j in range(power.size):
                if current_power>power[j]:
                    power=numpy.append(power,current_power)
    print(max(power))

















