import threading


def speak():
    print("hmmm")

def write():
    print("lovely")

t1=threading.Thread(target=speak)
t1.start()
t2=threading.Thread(target=write)
t2.start()

#t1.join()