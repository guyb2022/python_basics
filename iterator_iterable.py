"""
Iterable: something we can loop over it
It returns an iterator object from its __iter__() method
Iterator: something that has the __next__ and __iter__ method
This is an object with a state that hold it last place.
"""
# A list is iterable but it is not iterator
# it has the __iter__ method but not the __next__ method.
nums = [1,2,3]

# creating an iterator
i_nums = iter(nums) # ==  nums.__iter__()
print(i_nums)
# output: <list_iterator object at 0x000001D80597CE50>
print(next(i_nums))
# output: 1
print(next(i_nums))
# output: 2
print("part 1")

i_nums = iter(nums)
# Print all items:
while True:
    try:
        print(next(i_nums))

    except StopIteration:
        break
print("part 2")

# Build the class iterator
class MyRange:

    def __init__(self,start,end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

my_range = MyRange(1,3)
print(next(my_range))
# output: 1
print(next(my_range))
# output: 2
print(next(my_range))
# output: 3
print("part 3")

my_range = MyRange(1,3)
for i in my_range:
    print(i)
print("part 4")
# output:
# 1
# 2
# 3

# with generator function
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1
print("part 5")

my_nums = my_range(1,3)
for num in nums:
    print(num)
print("part 6")