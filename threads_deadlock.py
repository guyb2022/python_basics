import threading

# Create two locks
lock_a = threading.Lock()
lock_b = threading.Lock()

def function_a():
    lock_a.acquire()
    print("function_a doing somthing after lock_a aquired")
    lock_b.acquire()
    print("function_a doing somthing after lock_b aquired")
    lock_b.release()
    lock_a.release()

def function_b():
    lock_b.acquire()
    print("function_b doing somthing after lock_b aquired")
    lock_a.acquire()
    print("function_b doing somthing after lock_a aquired")
    lock_a.release()
    lock_b.release()

# Create two threads
t1 = threading.Thread(target=function_a)
t2 = threading.Thread(target=function_b)
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()