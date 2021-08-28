import threading
import time
semeaphore=threading.BoundedSemaphore(value=3)

def access_thread(thread_no):
    print(f"{thread_no} is trying to access!" )
    semeaphore.acquire()
    print(f"{thread_no} access granted!")
    time.sleep(10)
    print(f"{thread_no} thread is releasing")
    semeaphore.release()


for thread_number in range(1,11):
    t=threading.Thread(target=access_thread,args=(thread_number,))
    t.start()
    time.sleep(1)