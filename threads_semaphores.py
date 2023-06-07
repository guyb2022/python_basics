import threading
import time

semaphore = threading.BoundedSemaphore(value=2)

def access(thread_num):
    print(f"{thread_num} is trying to access!")
    semaphore.acquire()
    print(f"{thread_num} was granted access!")
    time.sleep(4)
    print(f"{thread_num} is now releasing!")
    semaphore.release()

for thread_num in range(1,5):
    t = threading.Thread(target=access, args=[thread_num])
    t.start()
    time.sleep(1)

