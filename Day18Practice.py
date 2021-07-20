# This is the 18th day of Python Practice
# I am back on learning more things in Python, instead
# of recapping and reinforcing my knowledge so far.
# Today, i will focus on learning a little more about
# function definitions and switch/case implementation

import inspect

def foo(arg):
    print("This is a ", arg)

# The foo() function is a standard function that accepts positional or keyword arguments

def foo1(*, arg):
    print("This function requires a keyword argument.")
    print(arg)

# The foo1() function only accepts keyword arguments. It does not accept positional arguments
# The asterisk symbol denotes that the arguments need to be keyword arguments

def foo2(arg, arg2, *arg3):
    print("The first two arguments are positional arguments")
    print("The arguments after the first two are packed into a tuple. This contains positonal arguments after the first two")
    print(arg)
    print(arg2)

    for arg in arg3:
        print(arg)

    argLength = len(inspect.getfullargspec(foo2))
    print("Argument Length:", argLength)

# The foo2() function accepts the first and second argument as 'arg' and 'arg2'.
# After the first two arguments, all positional arguments passed will be packed in a tuple called 'arg3'

def foo3(arg, *arg2, **keywordArg):
    print("First argument:", arg)
    for arg in arg2:
        print("Second argument:", arg)
    print("The third argument require keyword arguments!")

    for keyword in keywordArg:
        print(keyword, ":", keywordArg[keyword])

# The foo3() function accepts the first argument as 'arg', all positional arguments past the firs tone will be packed into 'arg2',
# and all keyword arguments will be packed into keywordArg dictionary.

foo("standard function")
foo(arg = "standard function 2.0")
foo1(arg = "cool")
#foo1("cool")
foo2("first arg", "second arg", 1, 2, 3, 4, 5)
foo3("Good Morning", "Positional", "Argument", "Two", one = "1", two = "2", three = "3")
