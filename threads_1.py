import threading
import time

done = False

def do_work_3(text):
    while not done:
        print(f"I'm a {text} seconds sleeper, leave me alone")
        time.sleep(3)

def do_work_1(text):
    while not done:
        print(f"I'm a {text} seconds sleeper, leave me alone")
        time.sleep(1)


t1 = threading.Thread(target=do_work_1, args=(1,))
t3 = threading.Thread(target=do_work_3, args=(3,))

t1.start()
t3.start()

input("press enter to quit\n")
done = True