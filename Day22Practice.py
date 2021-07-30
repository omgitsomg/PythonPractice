# Today is the 22nd day of Python practice.
# Today, I will focus on the 2nd part of 
# exception error handling.

# The try and exception statements have an else clause,
# which is useful when the try clause doesn't raise an exception.
# The example given in Python's documentation

#for arg in sys.arg[1:]:
#    try:
#        f = open(arg, "r")
#    except OSError:
#        print("cannot open", arg)
#    else:
#        print(arg, "has", len(f.readlines()), "lines")
#        f.close()

# In the example given, the try clause does not raise an exception, rather it opens up arg.
# If an error occurs, then the except clause catches the OSError.
# If there isn't any errors, then it prints out the number of lines the arg has.

# Exception Argument


try:
    raise Exception("First var", "Second var")
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print("x =", x, "\ny =", y)

# The try clause raises an exception with two arguments
# You can retrieve the two arguments simply by the statement "except Exception as inst"
# raise() allows the developer to force an exception to occur.
# Example

try:
    raise ZeroDivisionError()
except ZeroDivisionError:
    print("You cannot divide by 0!")

# The example forces the ZeroDivisionError to occur even though there aren't any numbers being divided by 0


# Exception Chaining
# The from keyword enables exception chaining
# Example

def foo():
    raise IOError
#try:
#    foo()
#except IOError as exc:
#    raise RuntimeError("Runtime error has occurred!") from exc

# To disable exception chaining, use the "from None"
# Example

#try:
#    foo()
#except IOError:
#    raise RuntimeError from None

# You can, also, define your own exceptions
# Your own defined exception should have attributes to display
# Examples

class exampleError(Exception):
    pass

class InputError(exampleError):
    """ Exception is raised for errors from the input

    Attributes:
        Expression - input expression in which the error occurred
        message - explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class randomError(Error):
    # This is to show how to define an error

    # Attributes:
        # number - number from input
        # message - explanation of the error

    def __init__ (self, number, message):
        self.number = number
        self.message = message

# The finally clause executes right before the try statement completes
# The clause executes regardless if an error occurs or not during the try clause
# If a finally clause has a return statement and the try statement has a return statement too, then
# the finally statement's return is returned.

try:
    raise KeyboardInterrupt
finally:
    print("Statement before the error")

