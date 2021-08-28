#Demon thread use for get the live updates and view it.
import threading
import time
content=""
def read():
    global content
    while True:
        with open("text.txt", 'r') as f:
            content=f.read()
        time.sleep(1)

def write():
    global content
    for i in range(30):
        print(content)
        time.sleep(1)


t1=threading.Thread(target=read,daemon=True)
t2=threading.Thread(target=write)

t1.start()
t2.start()
