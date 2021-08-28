import numpy as np

arr=np.array([[1,5,6],[58,7,54],[8,7,-5]])
print(arr)
max=arr.max()
max_axis_0=arr.max(axis=0)

print(max)
print(max_axis_0)
min=arr.min()
print(min)

sum=arr.sum()
print(sum)