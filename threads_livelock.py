import threading

# Create two locks
lock_a = threading.Lock()
lock_b = threading.Lock()

x = 10
def function_a():
    global x
    while True:
        lock_a.acquire()
        if lock_b.acquire(blocking=False):
            x += 1
            print(f"function_a doing somthing: {x}")
            lock_b.release()
            lock_a.release()
            break
        lock_a.release()

def function_b():
    global x
    while True:
        lock_b.acquire()
        if lock_a.acquire(blocking=False):
            x -= 1
            print(f"function_b doing somthing: {x}")
            lock_a.release()
            lock_b.release()
            break
        lock_b.release()

# Create two threads
t1 = threading.Thread(target=function_a)
t2 = threading.Thread(target=function_b)
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()