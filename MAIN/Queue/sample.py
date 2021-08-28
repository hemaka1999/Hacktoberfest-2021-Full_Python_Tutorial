import queue
#Default one is first in first out
q=queue.Queue()
numbers=[1,2,3,4,5,6,7,8]

for i in numbers:
    q.put(i)

print(q.get())
print(q.get())
print(q.get())