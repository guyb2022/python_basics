
from collections import Counter

def get_unique_chars(str1, str2):
    if len(str1) == 0:
        return str2
    elif len(str2) == 0:
        return str1

    char_count = Counter(str1) + Counter(str2)
    unique_chars = [char for char, count in char_count.items() if count == 1]
    return ''.join(unique_chars)

def unique_characters(str1, str2):
    if len(str1) == 0:
        return str2
    elif len(str2) == 0:
        return str1

    unique_chars = []
    char_count = {}

    for char in str1:
        # char_count.get(char, 0) will check if char_count[char]
        # is present in char_count. if exsist it will add 1 to its
        # counter. If it is not exsist, it will create it and update
        # its value to 0, So we will dont need to check if it was
        # alread in the char_count.
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        if count == 1:
            unique_chars.append(char)

    return ''.join(unique_chars)


str1 = ''
str2 = 'c'
print(unique_characters(str1,str2))
print(get_unique_chars(str1,str2))