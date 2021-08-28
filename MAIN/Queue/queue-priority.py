import queue

q=queue.PriorityQueue()

q.put((18,"hmm"))
q.put((16,"haa"))
q.put((10,"kk"))
q.put((17,"waa"))
q.put((11,"chaa"))

while not q.empty():
    print(q.get())
