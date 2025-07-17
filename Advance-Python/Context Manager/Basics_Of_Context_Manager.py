# ------------------- Context Managers in Python -------------------

# Context Managers are used to manage resources, ensuring that they are properly
# acquired and released. The most common example is file handling, but they are
# also useful for managing database connections, sockets, and more.

# **Basic Syntax:**
# with <context_manager> as <variable>:
#     <block of code>
# The context manager automatically handles resource cleanup.

# ------------------- 1. Using Context Manager for File Handling -------------------

# When you use the `with` statement, Python ensures the file is closed automatically,
# even if an error occurs within the block.

print("Using Context Manager for File Handling")

with open("example.txt", "w") as file:  # Open a file in write mode
    file.write("Hello, World!")  # Write to the file
    # No need to explicitly call `file.close()`

# Reading the same file
with open("example.txt", "r") as file:  # Open a file in read mode
    content = file.read()
    print("File Content:", content)
# The file is automatically closed here.

# ------------------- 2. Without Context Manager -------------------

# If you do not use a context manager, you must manually close the file.
print("\nWithout Context Manager")

file = open("example_no_context.txt", "w")  # Open the file
try:
    file.write("Hello without context manager!")
finally:
    file.close()  # Ensure the file is closed manually

# **Risk**: If you forget to call `file.close()`, the file remains open, causing resource leaks.

# ------------------- 3. Custom Context Managers -------------------

# You can create your own context manager using a class by implementing two methods:
# - `__enter__`: Code that runs when entering the context
# - `__exit__`: Code that runs when exiting the context

print("\nCustom Context Manager")

class CustomFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None  # Initialize file variable

    def __enter__(self):
        """Executed when entering the context (e.g., opening the file)."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file  # Return the file object

    def __exit__(self, exc_type, exc_value, traceback):
        """Executed when exiting the context (e.g., closing the file)."""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()  # Ensure the file is closed

# Using the custom context manager
with CustomFile("custom_example.txt", "w") as file:
    file.write("This file is managed by a custom context manager.")

# ------------------- 4. Handling Exceptions in Context Managers -------------------

# If an exception occurs within the `with` block, the `__exit__` method
# is still executed, allowing for cleanup. The exception details are passed to
# `__exit__` as parameters: `exc_type`, `exc_value`, `traceback`.

print("\nHandling Exceptions in Context Manager")

class SafeOperation:
    def __enter__(self):
        print("Starting a safe operation.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleaning up after operation.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress the exception

# Use SafeOperation and deliberately cause an error
with SafeOperation():
    print("Performing an operation.")
    raise ValueError("Something went wrong!")  # Deliberate exception

# The `ValueError` exception is suppressed due to `return True` in `__exit__`.

# ------------------- 5. Using Contextlib for Simpler Context Managers -------------------

# The `contextlib` module provides a decorator `@contextmanager`, which allows
# you to create context managers using generator functions.

from contextlib import contextmanager

print("\nUsing contextlib for Simpler Context Managers")

@contextmanager
def simple_file_manager(filename, mode):
    file = open(filename, mode)
    try:
        print(f"Opening file: {filename}")
        yield file  # Yield control to the `with` block
    finally:
        print(f"Closing file: {filename}")
        file.close()

# Using the contextlib-based context manager
with simple_file_manager("contextlib_example.txt", "w") as file:
    file.write("This file is managed by contextlib.")

# ------------------- 6. Real-World Example: Database Connection -------------------

# Context managers are not limited to files; they are also used for managing
# resources like database connections, network sockets, etc.

print("\nReal-World Example: Database Connection")

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        # Simulate database connection
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing database connection: {self.db_name}")
        self.connection = None  # Simulate closing the connection

# Using the DatabaseConnection context manager
with DatabaseConnection("EmployeeDB") as conn:
    print(f"Using connection: {conn}")

# ------------------- 7. Summary -------------------

# Context managers (`with` statement) simplify resource management by ensuring
# proper acquisition and release of resources.
# Key benefits:
# - Automatic cleanup (e.g., closing files or connections).
# - Cleaner code with less boilerplate.
# - Safer resource handling, even in cases of exceptions.

'''

Problem 1: File Read and Write Operations
Scenario:
You are a software engineer working on a text editor application. Your task is to:

Read a file and print its content line by line.
Write new content into a different file.
Ensure that the files are properly closed after performing the operations.
Keywords:

open(), read(), readline(), readlines(), write()
Problem 2: Appending Data to a File
Scenario:
You are working on a logging system for an application. Each time an event occurs, you need to:

Append a log message with a timestamp to a log file.
Ensure that the log file is not overwritten but only appended to.
Keywords:

open() with mode 'a' (append), write()
Problem 3: Counting Lines, Words, and Characters in a File
Scenario:
As part of a data analytics project, you are tasked to:

Count the number of lines, words, and characters in a given text file.
Display the results in a user-friendly format.
Keywords:

read(), split(), len()
Problem 4: File Copy
Scenario:
You are developing a backup script. Your task is to:

Copy the content of one file to another.
Handle cases where the source file might be empty or missing.
Keywords:

read(), write(), Exception Handling (try, except)
Problem 5: File Search
Scenario:
You are writing a utility to search for specific keywords in large log files. Your task is to:

Search for all lines containing a specific keyword in a file.
Write those lines to a new file called results.txt.
Keywords:

readlines(), in (membership operator), write()
Problem 6: Large File Handling with Iterators
Scenario:
You need to process a file that is too large to fit into memory. Your task is to:

Use an iterator to read the file line by line.
Process and print only the first 10 lines.
Keywords:

open(), Iterators (for line in file)
Problem 7: Binary File Operations
Scenario:
You are working on an image processing application. Your task is to:

Open a binary file (e.g., an image file).
Copy the binary content to another file.
Ensure the file operations are optimized for binary data.
Keywords:

open() with mode 'rb' (read binary), 'wb' (write binary)
Problem 8: Temporary Files
Scenario:
As part of a temporary storage system, you need to:

Create a temporary file, write data to it, and read it back.
Ensure the temporary file is automatically deleted after use.
Keywords:

tempfile module, NamedTemporaryFile
Problem 9: File Metadata Retrieval
Scenario:
You are creating a file management application. Your task is to:

Retrieve metadata of a file, such as its size, creation time, and last modified time.
Print this metadata in a human-readable format.
Keywords:

os.path.getsize(), os.path.getctime(), os.path.getmtime()
Problem 10: File Encryption and Decryption
Scenario:
You are developing a basic file encryption system. Your task is to:

Read the content of a text file.
Encrypt the content using a basic cipher (e.g., reverse the text).
Write the encrypted content into a new file.
Similarly, decrypt the file content.
Keywords:

read(), write(), String Manipulation ([::-1] for reversing)
Problem 11: File Renaming and Deleting
Scenario:
As part of a file cleanup utility, you are tasked to:

Rename a given file.
Delete a file if it meets certain conditions (e.g., it is empty).
Keywords:

os.rename(), os.remove()
Problem 12: File Compression
Scenario:
You are tasked with reducing storage space in a server. Your task is to:

Compress a text file into a .gz format.
Later, decompress the file back to its original format.
Keywords:

gzip module, open() with 'wt' (write text) and 'rt' (read text)
Problem 13: Directory Listing and File Search
Scenario:
You are creating a file explorer. Your task is to:

List all files in a directory.
Search for files with a specific extension (e.g., .txt) and write their names into a file called file_list.txt.
Keywords:

os.listdir(), os.path.join(), endswith()
Problem 14: Reading and Writing JSON Files
Scenario:
You are working with a web application that exchanges data in JSON format. Your task is to:

Read data from a JSON file.
Modify the data and save it back to the file.
Keywords:

json.load(), json.dump()
Problem 15: CSV File Handling
Scenario:
You are working on a data analysis project. Your task is to:

Read data from a CSV file.
Calculate the sum of a specific column (e.g., "sales").
Write the results into a new CSV file.
Keywords:

csv.reader(), csv.writer(), Iteration
Problem 16: File Path Validation
Scenario:
You are working on a script that processes files. Your task is to:

Check if a given file path exists.
If it exists, check whether it’s a file or a directory.
Keywords:

os.path.exists(), os.path.isfile(), os.path.isdir()
Problem 17: Multi-file Processing
Scenario:
You are tasked with merging multiple files into one. Your task is to:

Read data from multiple files.
Combine the content and write it to a single file called merged.txt.
Keywords:

open(), Iteration (for file in files)
Problem 18: File Permissions
Scenario:
You are working on a secure file system. Your task is to:

Change the permissions of a file to make it read-only.
Later, restore the file's original permissions.
Keywords:

os.chmod(), Permission Flags (stat.S_IREAD, stat.S_IWRITE)
Problem 19: File Tail Operation (Reading the Last N Lines)
Scenario:
You are implementing a logging utility. Your task is to:

Read and display the last N lines of a large log file efficiently.
Keywords:

seek(), readlines(), Slicing
Problem 20: Detecting and Removing Duplicates
Scenario:
You are working on a file management script. Your task is to:

Identify duplicate lines in a text file.
Write only unique lines to a new file.
Keywords:

readlines(), set(), Iteration
Summary of Keywords
Keyword	Usage
open()	Open a file for reading, writing, or appending.
read()	Read the entire file content as a string.
readline()	Read a single line from the file.
readlines()	Read all lines as a list of strings.
write()	Write content to a file.
os module	For file and directory operations.
json module	Reading and writing JSON files.
csv module	Handling CSV files.
gzip module	Compressing and decompressing files.
tempfile module	Creating temporary files.
os.path functions	Checking file existence, size, type, etc.
These scenarios will challenge you to explore various file-handling tasks using the with statement and essential Python file management concepts. Let me know if you’d like solutions or further details for any of the problems!

'''