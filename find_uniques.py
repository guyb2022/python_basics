from collections import Counter

def find_unique_2(arr):
    """ return items that appear only 1 time"""
    char_count = Counter(arr)
    return [char for char, count in char_count.items() if count == 1]

def find_uniqe(arr):
    """ Return a set of items"""
    ans = []
    for element in arr:
        if element not in ans:
            ans.append(element)

    return ans

def find_unique_3(arr):
    return set(arr)

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5, 5, 5]
print(find_unique_2(arr))
print(find_uniqe(arr))
print(find_unique_3(arr))