import threading

event_t=threading.Event()

def event():
    print("Event is waitting...")
    event_t.wait()
    print("Event is now working...")


t1=threading.Thread(target=event)
t1.start()
x = input("Do you want triggrer the event? y/n:")
if x=="y":
    event_t.set()



