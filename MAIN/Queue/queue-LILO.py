import queue
q=queue.LifoQueue()
numbers=[10,5,242,232,554]
for num in numbers:
    q.put(num)

print(q.get())
print(q.get())