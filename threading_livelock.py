import threading

class Spoon:
    def __init__(self, owner):
        self.owner = owner
        self.lock = threading.Lock()

    def pick_up(self):
        self.lock.acquire()

    def put_down(self):
        self.lock.release()

    def __str__(self):
        return self.owner


def eat_with(spoon1, spoon2):
    while True:
        spoon1.pick_up()
        if not spoon2.lock.acquire(blocking=False):
            print(f"{threading.current_thread()} swapping spoons")
            spoon1.put_down()
            continue
        break

    try:
        print(f"{threading.current_thread()} eating")
        # Simulating delay during eating
        threading.Event().wait()
    finally:
        spoon1.put_down()
        spoon2.put_down()


spoon1 = Spoon("Spoon 1")
spoon2 = Spoon("Spoon 2")

thread1 = threading.Thread(target=eat_with, args=(spoon1, spoon2))
thread2 = threading.Thread(target=eat_with, args=(spoon2, spoon1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

"""
In the provided livelock example, the output can indeed vary, and in some cases, you may observe only one
thread successfully acquiring both spoons and proceeding with the eating process while the other thread gets
stuck in the livelock condition.
This occurs when thread1 successfully acquires spoon1 and spoon2 in quick succession, while thread2 is
unable to acquire spoon2 due to the livelock condition.
As a result, only thread1 proceeds with the eating process, and thread2 remains stuck in the livelock.
"""