# Today is the 19th day of Python Practice.
# I will focus on input and output in Python.

# You can convert any value to a string with repr() and str() functions.
# Examples
string1 = "Kevin"
bool = True
num = 500
print(str(string1))
print(repr(string1))
print(repr(bool))
print(repr(bool), str(num))
# the repr() function adds single quotes if the variable is already a string, and
# it also adds any backslashes



# Formatted String Literals - They let you include value of Pytho expressions inside a string
# by simply putting a 'f' or 'F' at the beginning before the quotation mark

current_year = 2021
date = "July 21st"
print(f"Today is {date}, {current_year}.")
# The {date} refers to the date variable, while {current_year} refers to the current_year variable

num1 = 10
num2 = 15
num3 = 5
average = (num1 + num2 + num3) / 3
print("{:.3f} is the average of {:2}, {:2}, and {:2}.".format(average, num1, num2, num3))
# "{:.3f}" means truncate to the thousandth
# Useful .format types
# {:%} = percent form. Ex.) var = 20, {:.2%} = 25.00%
# {:d} = converts a number in binary into decimal number notation. var = 0b11, prints out '3'
# {:,} = adds a comma as a thousand separator. Ex) var = 15000, prints out 15,000
# {:-} = adds a negative sign if the number is negative. Ex) var = -5, prints out -5 but a positive 5 will only print 5
# {:+} = adds a negative or positive sign depending on the sign of the number. Ex.) var = 25, prints out '+25' or var = -25, prints out '-25'
# {:<}, {:>}, and {:^} = left aligns, right aligns, and center aligns.
# {:e} and {:E} are scientific format with lower case or upper case 'e'. Ex.) var = 25, prints out 2.5000000E+01 or 2.5000000e+01
# {:o} and {:x} are octal and hexidecimal format

print("{0} {1}".format("Hello", "Kevin"))
print("{1} {0}".format("Hello", "Kevin"))
# The numbers represent the position of the object being passed to .format

print("Goodmorning {name}, {greeting}".format(name = "Kevin", greeting = "How are you doing today?"))
# You can use keyword arguments, but the names have to be the same as the one in the brackets.
# Both positional and keyword arguments can in used together in .format()


idDict = {"Steven" : 123,
          "Max" : 456,
          "Tiffany" : 789}

print("Current Occupants in the elevator are Max: {0[Max]:d}, Tiffany: {0[Tiffany]:d}, and Steven: {0[Steven]:d}".format(idDict))
print("Current Occupants in the elevator are Max: {Max:d}, Tiffany: {Tiffany:d}, and Steven: {Steven:d}".format(**idDict))
# Using a dictionary to carry the values is a nice way of keeping the variables together.
# In addition, there are two ways of printing out values from a dict to a formatted string
# I use a ** to unpack the dictionary and use the same key names in the dict in the formatted string