import numpy as np

#array initiate
array1=np.array([[2,5,7,4,45],[5,8,6,2,4]])
print(array1)
#get shape
print(array1.shape)

#get dimension
print(array1.ndim)

#get type
print(array1.dtype)
print(array1.ctypes)


#specify the data type
array2=np.array([0,6,7,222,55,4],dtype="int16")
print(array2.dtype)# this showning you to size each item had(bits)

#get 1 item size(byte)
print(array1.itemsize,array2.itemsize)

#array_item_quantity
print(array1.size,array2.size)

#get total size
print(array1.size*array1.itemsize,array2.size*array2.itemsize)
print(array1.nbytes,array2.nbytes)

#get specific item array[c,r]
print(array1[0,4])
print(array2[5])

#get specific row
print(array1[0,: ])
array = np.arange(20)

#get specific column
print(array1[:,3])

#getting elements useful way
print(array1[0,0:5:2])

#replce items
array1[1,3]=22222
print(array1)

#replae row
array1[0,:]=222
print(array1)

#replace column
array1[:,2]=89
print(array1)

#empty array
arr=np.empty([2,],dtype='int16')
np.append(arr,[5,5])
print(arr,arr.shape)

#append array
array2=np.append(array2,([2,6,8]))
print(array2)

print(array)
print(array.shape)
d_array=np.array(array).reshape(4,5)
print(d_array)
print(d_array[0][1])

#all ones matrix
zero_array=np.zeros((2,3))
print(zero_array)

#all ones matrix
ones_array=np.ones((2,3))
print(ones_array)

#anyother number
any_all=np.full((2,2),9)
print(any_all)

#replace the full array from another number
any=np.full_like(any_all,4)
print(any)

#random number array
ran_array=np.random.rand(4,2)
print(ran_array)

get_previous_shape=np.random.random_sample(any.shape)
print(get_previous_shape)

int_integer_value=np.random.randint(5,10,size=(3,3))
print(int_integer_value)

#The identiy matrix
arr_i=np.identity(3)
print(arr_i)

#repeat an array
arr=np.array([[1,2,3]])
r1= np.repeat(arr,3,axis=0)
print(r1)

""""
11111
10001
10901
10001
11111

"""

result=np.ones((5,5))
print(result)

middle=np.zeros((3,3))
print(middle)
middle[1,1]=9
print(middle)
result[1:4,1:4]=middle
print(result)