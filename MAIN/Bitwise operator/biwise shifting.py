# 2 = 0b10
x=2 << 2
print(x)
# Out: 8
# 8 = 0b1000
y=bin(2 << 2)
print(y)
# Out: 0b1000
print(bin(7))
x=7 << 1
print(x)
# Out: 14
print(bin(x))

print(bin(3))
x=3<<3
print(x)
y=bin(x)
print(y)

#Bitwise right shift

# 8 = 0b1000
x=8 >> 2
# Out: 2
# 2 = 0b10
bin(8 >> 2)
print(x)
# Out: 0b10