import random

def randomize_array(array):
    """ Shuffle an array items by Knuth shuffle """
    n = len(array)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
randomize_array(numbers)
print(numbers)
