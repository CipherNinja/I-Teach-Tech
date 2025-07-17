# Problem 1: File Read and Write Operations
# Scenario:
# You are a software engineer working on a text editor application. Your task is to:

# Read a file and print its content line by line.
# Write new content into a different file.
# Ensure that the files are properly closed after performing the operations.
# Keywords:

# open(), read(), readline(), readlines(), write()


class filehandling:
    def __init__(self,file,mode):
        if not isinstance(file and mode,str):
            raise IOError("Wrong Input")
        self.filename = file
        self.mode = mode

    def openfile(self):
        try:
            file = open(self.filename,self.mode)
            return file
        except FileNotFoundError as notfound:
            raise FileNotFoundError(f"File not exists at :{self.filename}")
    def readfile(self):
        file = filehandling.openfile(self)
        return file.read()
        



print(filehandling(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\Context Manager\resources\index.html","r").readfile())