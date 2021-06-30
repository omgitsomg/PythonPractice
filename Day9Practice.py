# This is the 9th day of Python practice.
# Today, I will focus on inheritance in Python

# Using the Dog class I created, I will make a
# BengalCat class that will inherit the methods from
# the Cat class.
# In addition, I will learn about overriding methods
# in Python.


class BengalCat(Cat):


    def __init__(self, fur_texture = "coarse"):
        self.fur_texture = fur
        super(Meow = False, gender = "female", age = 7).__init__()
    def brush_fur(self):
        fur_texture = "soft"
    def wash_fur(self):
        fur_texture = "wet"

# In the BengalCat class, I overrided the __init__ function
# from the Cat class.
# To call the constructor from the parent class, you have to
# call the super() function. Within the super() call, I passed in
# the Meow, gender, and age variables.
# After the super() call, I added __init__ at the end to call that 
# function to initialize the fur_texture.