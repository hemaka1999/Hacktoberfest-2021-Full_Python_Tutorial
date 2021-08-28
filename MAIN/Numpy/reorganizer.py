import numpy as np

before_arr=np.array([[58,5,-9],[4,87,2],[7,6,9]])
after_arr=before_arr.reshape((9,1))
print(before_arr)
print(after_arr)

#vertically stacking verctors

v1=np.array([8,4,5])
v2=np.array([78,4,5])

v=np.vstack([v1,v2])
print(v)

#horizontal stacking vetors
h1=np.array([5,58,-8,8,-7])
h1=h1.reshape((5,1))
print(h1)
