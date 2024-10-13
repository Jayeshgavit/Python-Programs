import os

# retrieve current working directory
print(os.getcwd())
# retrieve list of file in current working directory
print(os.listdir())

# remdir() remove directory : but only empty files
# rmtree() remove non-empty directory 




'''
Here are some commonly used functions:

1. **`os.getcwd()`**: Returns the current working directory.
2. **`os.chdir(path)`**: Changes the current working directory to the specified path.
3. **`os.listdir(path)`**: Lists all files and directories in the specified path.
4. **`os.mkdir(path)`**: Creates a new directory at the specified path.
5. **`os.remove(path)`**: Deletes a file at the specified path.
6. **`os.rename(src, dst)`**: Renames a file or directory from `src` to `dst`.
7. **`os.path.exists(path)`**: Checks if a file or directory exists.

These functions help in file handling and system-level operations.
'''

