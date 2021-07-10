# This is the 10th day of Python Practice.
# Today, I will focus on Tuples, which are
# built-in sequence data types in Python.

# A tuple is immutable, uses parentheses, (), and
# it could be used as a key in a dictionary.

# How to create a Tuple
numbers_Tuple = (0, 1, 2)
print(numbers_Tuple)

# In addition, the parentheses are optional.
# One can be made without parentheses.

string_Tuple = "string", "are", "cool"
print(string_Tuple)

# Tuples can be created from Lists as well.
# For example,

tuple_from_List = tuple([1, 2, 3])
print(tuple_from_List)

# You can also create a tuple from multiple lists.
# For example

list1 = [0, 1, 2]
list2 = [3, 4, 5]

multi_list_tuple = (*list1, *list2)
print(multi_list_tuple)

# The '*' operator is used to unpack all the elements from an
# iterable data type into their own individual elements.

# You can assign multiple variables at once by unpacking a tuple
# For example,

Dog = ("male", 7, "Golden Retriever")
gender, age, breed = Dog
print(gender)
print(age)
print(breed)

# If you switch the positions of gender, age, and breed then you essentially
# change what the variables are initialized to.
# This is helpful when receiving multiple values from a function

# Similar to a string, each element of the tuple can be accessed by the index
# For example
print(Dog[0])
print(Dog[1])
print(Dog[2])

# Important thing to note about tuples are the fact that they are immutable
# You cannot add or remove elements from a tuple
# However, you can make a new tuple out of an old tuple
# For example

two_Dogs = (*Dog, "and", "female", 12, "French Bulldog")
print(two_Dogs)

# To get the length of a tuple, use len()
print(len(Dog))
print(len(two_Dogs))
print(len(Dog) + len(two_Dogs))

# List vs Tuple, Lists are mutable while tuples are immutable
# Set vs Tuple, you can have duplicate elements in tuples, but not in sets.

# To get a string representation of a tuple, use str()
stringOfTuple = str(Dog)
print(stringOfTuple)