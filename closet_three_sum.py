def find_closest_sum(numbers, target_sum):
    n = len(numbers)
    if n < 3:
        return []

    numbers.sort()  # Sort the array in ascending order
    closest_sum = float('inf')  # Initialize closest_sum to a large value
    result = []

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if current_sum == target_sum:
                # Exact sum found, return the numbers
                return [numbers[i], numbers[left], numbers[right]]

            # Check if the current sum is closer to the target sum
            if  current_sum <  closest_sum:
                closest_sum = current_sum
                result = [numbers[i], numbers[left], numbers[right]]

            if current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return result

# Example usage
numbers = [1, 5, 6, 8, 9, 10, 13]
target_sum = 21
closest_numbers = find_closest_sum(numbers, target_sum)
print(closest_numbers)