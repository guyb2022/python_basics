import multiprocessing

def square_queue(n, output_queue):
    result = n * n
    output_queue.put(result)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    processes = []
    output_queue = multiprocessing.Queue()

    for number in numbers:
        process = multiprocessing.Process(target=square_queue, args=(number, output_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while not output_queue.empty():
        result = output_queue.get()
        results.append(result)

    print(results)