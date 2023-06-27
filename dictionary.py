"""
Copying a dictionary without a loop
"""
dict1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
dict2 = {}

dict2.update(dict1)

print(dict2)