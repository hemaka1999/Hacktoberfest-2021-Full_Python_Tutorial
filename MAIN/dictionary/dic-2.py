words=[8,98,67,362,901,321,4,22,1,1,12,4,8,8,5,3,75,3,643,89,43,22,67,43]
y=dict()
num=0
for word in words:
    y[word] = y.get(word, 0) + 1

print(y)