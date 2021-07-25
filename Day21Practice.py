# Today is day 21 of Python Practice.
# Today, I will focus on learning about exception handling
# in Python.
# This will be part 1.

# Python doesn't have a try catch like Java does, but it does have something
# similar called try except.

import sys

def divideBy0(num):
    return (num / 0)

try:
    divideBy0(10)
except ZeroDivisionError:
    print("ERROR! ")
    print("You cannot divide by 0!")

boolCorrectInput = True
while boolCorrectInput:
    try:
        print("Please enter a number:")
        x = int(input())
    except ValueError:
        print("Your input is not a number!")
        boolCorrectInput = False

# input() function simply grabs the input of the user.
# int() function simply converts the argument passed in into an int

# You can have more than one except clause for a try statement
# For example,

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for BCD in [B, C, D]:
    try:
        raise BCD
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# The last except can be used to used to catch all exception
# if the previous exception couldn't catch it

try:
    print("Enter a number:")
    y = int(input())
except ZeroDivisionError as zeroErr:
    print("{zeroErr} has occured! You cannot divide by 0!}".format(zeroErr))
except OSError as osErr:
    print("{osErr} has occurred!".format(osErr))
except:
    print("A random error has occurred!", sys.exc_info()[0])
