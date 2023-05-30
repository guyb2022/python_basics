
try:
    f=open('file_name.txt')
    if f.name == 'currupted_file.txt':
        raise Exception
# Specific exception
except FileExistsError as e:
    print(e)
# General exception
# Or one we got by using raise
except Exception as e:
    print("Bad File....")
# do somthing after open the file succesfuly with no error
else:
    pass
# Will happen no matter error or not
finally:
    print("executing Fianlly....")