import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def acquire_locks():
    lock1.acquire()
    print("Lock 1 acquired from thread1")
    # Simulating delay to increase the likelihood of a deadlock
    threading.Event().wait()
    lock2.acquire()
    print("Lock 2 acquired from thread1")
    lock2.release()
    lock1.release()

def acquire_locks_reversed():
    lock2.acquire()
    print("Lock 2 acquired from thread2")
    # Simulating delay to increase the likelihood of a deadlock
    threading.Event().wait()
    lock1.acquire()
    print("Lock 1 acquired from thread2")
    lock1.release()
    lock2.release()

thread1 = threading.Thread(target=acquire_locks)
thread2 = threading.Thread(target=acquire_locks_reversed)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# The reasult will be a stuck process
# thread1 acquired lock 1
# thread2 acquired lock 2
# both threads blocking each other

# Lock 1 acquired from thread1
# Lock 2 acquired from thread2