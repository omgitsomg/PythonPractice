# Today is the sixth day of Python practice.
# I will focus on learing about functions in Python
# and how they work.

# First part of a function is the keyword "def"
# After "def" comes the function name, the parentheses,
# and the colon

# Example 1
# This function starts with "def" and then the 
# function name of "print_Hello-World".
# At the end of the statement, there are parentheses
# and the colon.
# To show that statements are within the scope
# of the function, you must indent the statements all on
# the same indentation

def print_Hello_World():
    print("Hello World!")


print_Hello_World()

# Example 2
# Just like in C and Java, you can pass arguments
# to functions.
# In this example, I pass in my name to the function
# called greetings

def greetings(name):
    print ("Hello", name, "\nHow are you doing today?")
    # This print statement below prints the same string
    # as the statement above.
    # print ("Hello" + name + "\nHow are you doing today?")

greetings("Kevin Ly")

# Example 3
# Variables defined on the top-level of a program are
# visible in all the code.
# As you can see below, the name variable is defined and initialized
# outside the greetings function, but it can still be used
# within the function
# In Java object-oriented programming, this would not have work.
# We would have to pass the variable to the function and have the function
# contain a parameter

name = "Kevin Ly"
def greetings():
    print ("Hello", name, "\nHow are you doing today?")

greetings()

# Example 4
# This example shows that functions can, also, use multiple arguments
# just like Java and C programming
# You don't have to use the named parameters like "planet =" or
# "adjective =".
# However, positions do matter in the parameters
# For example, for "planets(adjective = "hot")"
# if we removed the named parameter, the function will make "hot" into
# the name of the planet
# This is called positional parameters


def weather(location, temperature):
    print("Today's temperature in", location, "is", temperature)

weather("Virginia Beach", "76 degrees Fahrenheit")
print()

def planets(planet = "Earth", adjective = "cool"):
    print("This planet called", planet, "is", adjective)

planets()
planets(planet = "Venus")
planets(adjective = "hot")
planets(planet = "Venus", adjective = "hot")

