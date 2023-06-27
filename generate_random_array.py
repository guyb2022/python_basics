import random

def generate_random_array(N):
    return random.sample(range(1, N+1), N)


# Example usage
N = 10  # Size of the array
random_array = generate_random_array(N)
print(random_array)