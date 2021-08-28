import threading
import time
x=4096
lock=threading.Lock()
def double():
    global x,lock
    lock.acquire()
    while x<4096:
        x*=2
        print(x)
        time.sleep(1)
    print("Become to max")

    lock.release()

def half():
    global x,lock
    lock.acquire()
    while x>1:
        x/=2
        print(x)
        time.sleep(1)
    print("Become a minimum")
    lock.release()

t1=threading.Thread(target=double)
t2=threading.Thread(target=half)
t2.start()
t1.start()
