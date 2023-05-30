import multiprocessing
import ctypes

def square_array(n, output_array, index):
    result = n * n
    output_array[index] = result

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    num_processes = len(numbers)
    output_array = multiprocessing.Array(ctypes.c_int, num_processes)

    processes = []
    for i, number in enumerate(numbers):
        process = multiprocessing.Process(target=square_array, args=(number, output_array, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = list(output_array)
    print(results)