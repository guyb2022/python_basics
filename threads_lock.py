import threading
import time

x = 3
lock = threading.Lock()

def add():
    global x,lock
    # lock.acquire()
    while x < 10:
        x += 1
        print(x)
        time.sleep(1)
    print("Reached maximum value!")
    # lock.release()

def subs():
    global x,lock
    # lock.acquire()
    while x > 1:
        x -= 1
        print(x)
        time.sleep(1)
    print("Reached minimum value!")
    # lock.release()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=subs)

t1.start()
t2.start()

t1.join()
t2.join()