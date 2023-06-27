def remove_duplicate(arr):
    if len(arr) <= 1:
        return arr  # No duplicates to remove

    write_index = 1  # Index to write unique elements

    for i in range(1, len(arr)):
        if arr[i] not in arr[:write_index]:
            arr[write_index] = arr[i]
            write_index += 1

    # Truncate the array to remove any remaining elements
    del arr[write_index:]

    return arr

# Example usage
arr = [1, 2, 3, 4, 2, 5, 6, 1, 3]
remove_duplicate(arr)
print(arr)  # Output: [1, 2, 3, 4, 5, 6]
