import threading
import time

def simple_func():
    for _ in range(3):
        print("I'm a simple func")
        time.sleep(1)

t1 = threading.Thread(target=simple_func, daemon=True)
t1.start()
time.sleep(2)
t1.join()


