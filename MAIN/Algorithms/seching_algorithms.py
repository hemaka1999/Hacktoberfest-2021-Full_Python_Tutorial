#leanear serching
list_1=[56,8,74,9,23,47,32,15]
x=74
for i in range(len(list_1)):
    if list_1[i]==x:
        print(i)

#Binary search
list_2=[8,87,96,45,47,23]

def binary_search(l,x):
    mid=len(l)//2

    if l[mid]==x:
        return l[mid]
    elif x>l[mid]:
        return binary_search(l[mid: ],x)
    else:
        return binary_search(l[ :mid],x)
result=binary_search(sorted(list_2),87)
print(list_2.index(result))