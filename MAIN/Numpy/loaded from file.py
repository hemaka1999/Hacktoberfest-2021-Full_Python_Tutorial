import numpy as np
file_data=np.genfromtxt('1.txt',delimiter=',')
file_data=file_data.astype('int32')
print(file_data)
print(file_data>50)
print((file_data>=500) & (file_data<100))
