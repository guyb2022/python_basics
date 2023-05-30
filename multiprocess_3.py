import multiprocessing
import concurrent.futures
import time

def do_somthing_multi(seconds):
    print(f'Program Sleeping {seconds} second...')
    time.sleep(seconds)
    print(f'program do_somthing_multi Done Sleeping {seconds} second(s)...')

def do_somthing_conc(seconds):
    print(f'Program Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'program do_somthing_conc Done Sleeping {seconds} second(s)...'

if __name__ == '__main__':

    proccesses = []
    #One method
    start = time.perf_counter()
    for sec in range(5):
        p = multiprocessing.Process(target=do_somthing_multi, args=[sec])
        # start the process
        p.start()
        proccesses.append(p)

    for process in proccesses:
        # wait for the process to finish
        process.join()

    finish = time.perf_counter()
    print(f"Finished first method in {round(finish - start,2)} second(s)")
    print("*"*10)
    # Seconf method
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executer:
        results = [executer.submit(do_somthing_conc, sec) for sec in range(5)]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f"Finished second method in {round(finish - start,2)} second(s)")
    print("*"*10)
    # third method
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executer:
        secs = [1,2,3,4,5]
        results = executer.map(do_somthing_multi, secs)

    finish = time.perf_counter()
    print(f"Finished third method in {round(finish - start,2)} second(s)")

