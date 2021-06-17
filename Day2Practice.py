# This is a single comment line.

# To create a single line comment. Append '#' at the beginning of the line.


# To create a multiline comment,
# just append a '#'
# It is similar to the single comment line.
#
#
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
#
# To comment out multiple lines of code on Visual Studio,
# you just highlight the lines and hit CTRL+K+C.
# To uncomment the multiple lines of code,
# hit CTRL+K+U.
#
# To run a certain file in Visual Studio, go to 
# the project settings and change the Startup file to the
# file you want to run.
#
# To send a single line to the interactive, hit CTRL+ENTER
#
# To autocomplete on Visual Studio, hit the TAB button.
#
# This is day 2 of my Python practice over the summer.
# Today I will focus on string manipulation in Python.
# This is the URL of where I learned most of the things in Python.
# https://python.land/python-tutorial


# Strings in Python can be created with one character, the apostrophe.
str = 'Hello World'
print(str)

# They can, also, be made using quotation marks.
str2 = "Hello World"
print(str2)

# Using the '+' to concatenate strings.
str3 = 'a' + 'b'
print(str3)

# To duplicate something 'x' times
str4 = "abc" * 3
print(str4)

# To use an apostrophe in a single quote
str5 = 'it\'s an escaped quote'
print(str5)

# This is for double quotes in a double quote string.
str6 = "\"double quote\", John said"
print(str6)

# Multiline strings are created using triple quotes
str7 = """This
is
a
multiline string"""
print(str7)

# Some common string operations
testString = "kevin ly"

# Capitalizes the first letter of the string.
print(testString.capitalize())

# Turns all the letters to lowercase letters.
print(testString.lower())

# Returns true if the string is a decimal. Otherwise, return false.
print(testString.isdecimal())

# Returns true if the string ends with the argument. Otherwise, return false.
print(testString.endswith("ly"))

# Returns the index of where the argument is.
print(testString.find("v"))