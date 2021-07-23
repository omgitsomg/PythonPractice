# Today is the 20th day of Python practice.
# This will be a continuation of what I learned from Day 19,
# which is input and output.


f = open("examplefile", "r+")
# open("filename", "mode")
# first argument is a string containing the filename and second is
# how the file can be interacted with
# r is file read only
# w is file write only
# a is file appending, anything written to the file is added to the end
# r+ is both reading and writing
# If mode is left empty, then 'r' is assumed


#with open("examplefile") as f:
#    example_data = f.read()
#    pass

# Using the "with" keyword should be used when working with file objects.
# The advantage is the file properly closes after it finishes.
# If you are not using "with", then you need to use "f.close()", to free up system resources.
# Using the file after closing it will return an error.


print(f.write("This is the first line\n"))
print(f.write("This is the second line\n"))
for line in f:
    print(line, end="")

# f.write(string) simply writes the string to the file and it returns the number of characters written in the file.
# To print the lines from a file, you can use a for loop to loop through the file object and print it line by line.
# This is memory efficient, fast, and simple code.

# Useful file methods
# f.tell() = returns an integer giving the file object's current position in the file represented as number of bytes
# from the beginning of the file when in binary mode and an opaque number when in text mode.
# f.seek(offset, whence) = to change the file object's position. The offset is used to calculate how far you want to go from the reference point,
# and the whence value has a couple of options
# 1 = current file position
# 2 = end of the file as reference point.
# When whence is omitted, it defaults to "0", which uses the beginning of the file as the reference point.