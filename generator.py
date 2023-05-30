"""
Generators don't hold the entire result in memory.
It is waiting for us to call it in each time,
and it yield the answer one at a time.
The __iter__ and __next__ are created automatically.
The position of the state is saved to the current location.
"""

def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

def square_numbers_generator(nums):
    for num in nums:
        yield num*num
my_nums_gen = square_numbers_generator([1,2,3,4,5])
# we can use the same syntax as follow:
my_nums_gen_2 = (x*x for x in [1,2,3,4,5])
# This will create a generator like the above

# to print one at a time without buffering the entire list
for num in my_nums_gen:
    print(num)
# We can fill out the memory with the entire list.
# But loose the efficiency as with the yield
print(list(my_nums_gen))

# Another way is to use the list comprehension.
# This is also will fill the memory with the entire list
my_nums_gen_2 = [x*x for x in [1,2,3,4,5]]
print(my_nums_gen_2)
