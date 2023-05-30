import os
from datetime import datetime

# get current path
print(os.getcwd())

# change directory:
# os.chdir('new_path')
# Make dir
# os.mkdir('new_path)
# make sub dirs
# os.mkdirs('new_path)
# remove dir
# os.rmdir('path_to_dir')
# os.removedirs('path_to_dir')
# rename file
# os.rename('old_file', 'new_file')
# file statistics
print(os.stat('os.py'))
print(f"size: {os.stat('os.py').st_size}")
print(f"created at: {datetime.fromtimestamp(os.stat('os.py').st_mtime)}")
#
# go over the directory tree recursevly
# for dirpath, dirnames, filenames in os.walk('path'):
#     print(f'Current Directory: {dirpath}')
#     print(f"Directories: {dirnames}")
#     print(f"Files: {filenames}")
#     print()

# concatinate path veraibles
print(os.path.join(os.environ.get('HOMEPATH')))
file_path = os.path.join(os.environ.get('HOMEPATH'), 'os.py')
print(file_path)