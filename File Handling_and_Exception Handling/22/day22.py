# Day 22: Reading and Writing Files



'''
open() function is used to open a file in Python. It takes two arguments:
1. filename: The name of the file to be opened.
2. mode: The mode in which the file should be opened. It can be one of the following:
    "r" (read mode) # reads the file
    "w" (write mode) # overwrites the file if it already exists and creates a new file if it doesn't
    "a" (append mode) # appends the content to the end of the file
    "r+" (read/write mode) # opens the file for both reading and writing
    "w+" (write/read mode) # overwrites the file if it already exists and creates a new file if it doesn't
    "a+" (append/read mode) # appends the content to the end of the file
'''

# write() function is used to write content to a file.
# close() function is used to close a file.


# Writing to a file
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()
print("File written successfully.")



# Reading a file

'''
read() returns the entire content of the file as a string.
readlines() returns a list of lines in the file.
'''
file = open("example.txt", "r")
content = file.read() # returns a string
file.close()
print(content)




# Appending to a file
file = open("example.txt", "a")
file.write("\nGoodbye, world!")
file.close()
print("File appended successfully.")