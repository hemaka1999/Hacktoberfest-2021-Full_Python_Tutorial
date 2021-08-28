import numpy as np

arr=np.array([1,2,3])
arr=arr+123
print(arr)
arr=arr/5
print(arr)
arr2=np.array([6589,666,552])
x=arr+arr2
print(x)
print(np.sin(arr))
x=np.array([[5,6,36],[9,5,7]])
x=x.reshape(3,2)
print(x)
y=np.array([[5,6,2],[58,9,36,]])
p=np.matmul(y,x)
print(p)

#find the determinate
det=np.identity(3)
det=np.linalg.det(p)
print(det)

#trace

#singular vector decomposition

#Eigenvalues

#Matrix Norm

#Inverse

