import multiprocessing
import concurrent.futures
import time
import ctypes

def square_queue(n, output_queue):
    result = n * n
    output_queue.put(result)


def square_array(n, output_array, index):
    result = n * n
    output_array[index] = result

def square(n):
    return n * n

numbers = [i for i in range(1,100)]

if __name__ == '__main__':

###################### Using Queue ############################
    # Reset starting time
    t1 = time.perf_counter()
    processes = []
    # Using Queue for inter-process communication
    output_queue = multiprocessing.Queue()

    for number in numbers:
        process = multiprocessing.Process(target=square_queue,
                                          args=(number, output_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while not output_queue.empty():
        result = output_queue.get()
        results.append(result)

    t2 = time.perf_counter()
    print(f"Finished in {round(t2-t1,3)}")

######################## Using Array  ###########################
    # Reset starting time
    t1 = time.perf_counter()
    # Using Array and process number for inter-process communication
    num_processes = len(numbers)
    output_array = multiprocessing.Array(ctypes.c_int, num_processes)

    processes = []
    for i, number in enumerate(numbers):
        process = multiprocessing.Process(target=square_array,
                                          args=(number, output_array, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = list(output_array)
    t2 = time.perf_counter()
    print(f"Finished in {round(t2-t1,3)}")

#####################  Using multiprocessing.Pool  #####################
    # Reset starting time
    t1 = time.perf_counter()
    # Create a multiprocessing Pool
    pool = multiprocessing.Pool()

    # Apply the square function to each number in parallel using map()
    results = pool.map(square, numbers)
    # Calculate end time
    t2 = time.perf_counter()
    print(f"Finished in {round(t2-t1,3)}")

############# Using concurrent.futures.ProcessPoolExecutor ############
    # Reset starting time
    t1 = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executer:
        # Apply the square function to each number in parallel using map()
        results = executer.map(square, numbers)

    t2 = time.perf_counter()
    print(f"Finished in {round(t2-t1,3)}")

