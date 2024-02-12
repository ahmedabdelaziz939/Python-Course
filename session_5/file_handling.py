## creating file 
with open("new.txt", 'w') as file:
    file.write("Hello, Python!\n")
    file.write("This is a new file.\n")
    file.write("Writing to files is fun.")

## Opening and Closing Files
"""
   - Introduce the `open()` function for opening files.
   - Explain the different modes for opening files (`'r'` for read, `'w'` for write, 
         `'a'` for append,  etc.).
   - Emphasize the need to close files using the `close()` method.
   """
# ## Example: Opening and closing a file for reading
# file_path = 'new.txt'
# file = open(file_path, 'r')
# # Perform file operations here
# file.close()

## Reading from Files:**
"""
Explain methods for reading from files:
- `read()`: Reads the entire content of the file.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines into a list.
"""
# # Example: Reading from a file
with open('new.txt', 'r') as file:
       content = file.read(3)
       print(content)

## Writing to Files:
"""
Explain methods for writing to files:
    - `write()`: Writes a string to the file.
    - `writelines()`: Writes a list of strings to the file.
"""
# ## Example: Writing to a file
# with open('new.txt', 'a') as file:
#     file.write('Hello, Python!\n')
#     file.write('This is a new line.')

# ## Appending to Files:
# # Example: Appending to a file
# with open('example.txt', 'a') as file:
#     file.write('\nAppending additional content.')



## Handling File Exceptions:
"""- Discuss potential errors when working with files (e.g., `FileNotFoundError`, 
    `PermissionError`) and the need for error handling.
"""
# Example: Handling file exceptions
# try:
#     with open('nonexistent_file.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError as e:
#     print(f"Error: {e}")
# finally:
#     print("File handling complete.")

## Using `with` Statement:'
"""
- Explain the `with` statement for automatic resource management.
- Highlight its advantages, such as automatically closing files.
"""
# # Example: Using 'with' statement
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
# # File is automatically closed outside the 'with' block

## Seeking and Telling:
"""
   - Explain the `seek()` and `tell()` methods for file positioning.
   - Discuss scenarios where these methods are useful.
"""
# Example: Seeking and telling in a file
# with open('example.txt', 'r') as file:
#     file.seek(5)  # Move the cursor to the 5th position
#     content = file.read(3)  # Read 3 characters from the current position
#     position = file.tell()  # Get the current position
#     print(content, position)
# file_path = 'example.txt'

# with open(file_path, 'r') as file:
#     # Move cursor to the start of the 5th line (assuming each line ends with a newline character)
#     file.seek(0)  # Move to the beginning of the file
#     for _ in range(4):  # Move to the end of the 4th line
#         file.readline()
    
#     # Read the 5th line
#     fifth_line = file.readline()
#     print("5th Line:", fifth_line)
