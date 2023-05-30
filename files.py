# readign the whole file at once.
# good for small files, bad for memory with large files
with open('test.txt','r') as f:
    f_content = f.read()
    print(f_content)

# REading in chunks
with open('test.txt','r') as f:
    size_to_read = 10 # num of charecters
    f_content = f.read(size_to_read)

    f.seek(0) # go to position chrecter 0
    f.tell() # what is your current position

    while len(f_content) > 0:
        print(f_content, end='')
        f_content = f.read(size_to_read)


# read the file line by line, without exhausting the memory
with open('test.txt','r') as f:
    f_content = f.readlines()
    print(f_content)

# read the file line by line, same as above
with open('test.txt','r') as f:
    for line in f:
        print(line, end='')