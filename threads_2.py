import threading
import concurrent.futures
import time

def do_work_threads(text):
    """ Simple func to do some work """
    print(f"I'm a {text} seconds sleeper, leave me alone")
    time.sleep(int(text))

start = time.perf_counter()
t1 = threading.Thread(target=do_work_threads, args=[3])
t3 = threading.Thread(target=do_work_threads, args=[1])

# Start the threadings
t1.start()
t3.start()

# This will hold the program untill t1 & t3 will finish running
t1.join()
t3.join()

end = time.perf_counter()
print(f"program finished in {round(end-start,2)} second(s)'")

# use a loop
start = time.perf_counter()
threads =[]

for _ in range(5):
    t = threading.Thread(target=do_work_threads, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"program finished in {round(end-start,2)} second(s)'")

# # use context manager
def do_work_concurent(text):
    """ Simple func to do some work taking a parameter """
    print(f"I'm a {text} second(s)' sleeper, leave me alone")
    time.sleep(int(text))
    return f"Done Sleeping...{text} second(s)'"

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executer:
    f1 = executer.submit(do_work_concurent, 1)
    f3 = executer.submit(do_work_concurent, 3)
    print(f1.result())
    print(f3.result())

end = time.perf_counter()
print(f"program finished in {round(end-start,2)} second(s)'")

# another example using as_completed
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [3,2,1]
    results = [executer.submit(do_work_concurent, sec) for sec in secs]

    # as_completed print the threads in the order they are done.
    for f in concurrent.futures.as_completed(results):
        print(f.result())

end = time.perf_counter()
print(f"program finished in {round(end-start,2)} second(s)'")

# another example using map
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [3,2,1]
    results = executer.map(do_work_concurent, secs)

    for result in results:
        print(result)
# exception will be raised once the value will be return from the thread

end = time.perf_counter()
print(f"program finished in {round(end-start,2)} second(s)'")

# using class overiding the run method
class MyThreads(threading.Thread):
    def run(self):
        # code to be executed in the thread
        print("I'm a class thread!")

# Create and the start the thread
t = MyThreads()
t.start()

