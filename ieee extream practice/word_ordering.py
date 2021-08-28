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
from collections import defaultdict

word_order=dict()
def split(word):
    return [char for char in word]
char_order=split(get_word())

order2={i+26:char_order[i].upper() for i in range(len(char_order))}
order1={i:char_order[i] for i in range(len(char_order))}
order={**order1,**order2}
num=get_number()
number=list()
key_list = list(order.keys())
val_list = list(order.values())
key_order=list()
word_list=list()

for i in range(num):
    c_count=26
    new_word=split(get_word())

    key_order.clear()
    for char in new_word:

        if char in val_list:
            key_order.append(val_list.index(char))
        # else:
        #     c_count=27
        #     key_order.append(str(c_count))
    word_list.append(key_order.copy())
    # print(word_list)
sorted_list=sorted(word_list)


for i in range(len(sorted_list)):
    x=""
    for j in range(len(sorted_list[i])):
        x=x+order[sorted_list[i][j]]
    print(x)










