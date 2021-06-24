# This is the 7th day of practicing Python
# Today, I will focus on classes and objects


# I will create a class called Dog for practice
# and as an example to look back on

class Dog:
    age = 3
    gender = "male"
    dog_hungry = True

    def gender(self, dogGender):
        self.gender = dogGender
        print("The dog is a", self.gender, ".")

    def age(self, age):
        self.age = age
        print("The dog is", self.age, "years old.")

    def feedTheDog(self):
        self.dog_hungry = False
        print("The dog is now full!")

    def isDogHungry(self):
        if self.dog_hungry == True:
            print("The dog is hungry, and it wants dog treats.")
        else:
            print("The dog is full. The dog does not want anymore treats.")

dog1 = Dog()
dog1.gender("male")
dog1.age(10)
dog1.feedTheDog()
dog1.isDogHungry()

# I've created the Dog class, which have the methods gender, age, feedTheDog, and isDogHungry.
# The Dog class has three variables called age, gender, and dog_hungry
# The self variable within the methods refers to to itself essentially to operate on a variable
# that is part of the instance.