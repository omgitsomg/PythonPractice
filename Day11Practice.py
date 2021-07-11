# This the 11th day of Python Practice
# Today, I will focus on keyword arguments,
# decorators, anonymous functions, and * and ** operators

# Keyword arguments are arguments that you pass in with a variable attached to them
# Keyword arguments do not rely on positions.

# To force a keyword argument to be passed into the function,
# you simply put a * at the beginning of the function parameter
# For example

def divide_x_by_y(*, x, y):
    result = x / y
    return result

#result = divide_x_by_y(2,3)
# The statement above this comment gives an error message that reads
# "divide_x_by_y() takes 0 positional arguments but 2 were given"

result = divide_x_by_y(x = 2, y = 3)
print(result)
result2 = divide_x_by_y(y = 4, x = 2)
print(result2)
# By providing what numbers are attached to what variable,
# the function will know what variable is being divided by what.

# To unpack dictionaries that are sent to functions, you use the ** operator

xy_Dictionary = {"x" : 4,
                 "y" : 1}
print(divide_x_by_y(**xy_Dictionary))
xy_Dictionary2 = {"y" : 4,
                 "x" : 1}
print(divide_x_by_y(**xy_Dictionary2))

# To unpack arrays and lists that are sent to functions, you use the * operator

def printArray (a, b, c, d):
    print(a, b, c, d)
arr1 = [0, 1, 2, 3]
printArray(*arr1)

# Decorators are wrappers around a function that allows modification in a specific way.
# For example

def print_argument(func):
    def wrapper(num):
        print("The argument for", func.__name__ , "is", num)
        return func(num)

    return wrapper

@print_argument
def multiplyByThree(number):
    return number * 3

print(multiplyByThree(4))

# As you can see above, the decorator part is "@print_argument" line.
# Within the print_argument() function, the wrapper function prints out a statement.
# That statement grabs the function's name and the argument being passed to that function.
# It, then, returns the result of the multiplyByThree() function with the argument being passed to it.


# Anonymous functions are functions that are simple, and
# are normally used once.
# For example

multiplyByTwo = lambda x : x * 2
product = multiplyByTwo(10)
print(product)

# Above, the lambda keyword is assign to the variable x. 
# Whatever is passed to multiplyByTwo, that will be assigned to the variable "x".

add_five = map(lambda x : x + 5, arr1)
print(list(add_five))

# The map() function above applies the function to every individual element of the list.
# The list() function takes in an iterable data type and returns the list.