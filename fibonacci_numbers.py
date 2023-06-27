
def fibonacci_numbers(n):
    ans = [0, 1]

    for i in range(2, n):
        ans.append(ans[i-2] + ans[i-1])

    return ans

def fibonacci_numbers_2(n):
    ans = [0, 1]
    while(len(ans) < n):
        ans.append(ans[-2] + ans[-1])
    return ans

print(fibonacci_numbers(10))
print(fibonacci_numbers_2(10))