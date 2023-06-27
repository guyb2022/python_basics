
def find_missing_number(arr, n):
    """ Find missing value from a 1-n array """
    sum_arr = sum(arr)
    expected_sum = (n*(n+1)/2)

    return int(expected_sum - sum_arr)

arr = [1,2,3,4,5,6,7,9,10]
print(find_missing_number(arr, 10))