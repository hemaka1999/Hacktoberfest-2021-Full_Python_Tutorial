import os

path = "F:\Societies"
## Check if path exists
x=os.access(path, os.F_OK)
print(x)
## Check if path is Readable
y=os.access(path, os.R_OK)
print(y)
## Check if path is Wriable
z=os.access(path, os.W_OK)
print(z)
## Check if path is Execuatble
os.access(path, os.EX_OK)