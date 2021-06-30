# This is the 8th day of Python Practice
# Today, I will focus on constructors in Python

# I've created the Cat class with ideas from the Dog Class
# to help create it.

class Cat:
    
    def __init__(self, Meow = False, gender = "male", age = 3):
        self.Meow = Meow
        self.gender = gender
        self.age = age

    def gender(self, catGender):
        self.gender = catGender
        print("The cat is a", self.gender, ".")

    def age(self, age):
        self.age = age
        print("The cat is", self.age, "years old.")

    def Meow(self):
        print("The cat wants your attention. Maybe it wants some food.")
        self.Meow = True

    def isCatHungry(self):
        if self.Meow == True:
            print("The cat is hungry, and it wants cat food.")
        else:
            print("The cat is full. The cat does not want anymore food.")


# In the Cat class above, I created an __init__ method.
# This will give the User a chance to create a default 
# or an instance of a Cat object with values passed in.
# Below gives us some ideas
# The first cat makes a Cat object with default values
# The second creates a Cat object with the Meow variable 
# set to True
# The third creates a Cat object with True and gender set 
# to female
# Last, the fourth one creates a Cat object with true, female,
# and age set to 5. The Cat object will have the values of
# Meow = true, gender = "female", and age = 5.

cat1 = Cat()
cat2 = Cat(True)
cat3 = Cat(True, "female")
cat3 = Cat(True, "female", 5)
cat4 = Cat(Meow = False,gender = "male", age = 10)

cat2.isCatHungry()
cat4.isCatHungry()
cat4.Meow
cat4.isCatHungry()
