# Today is the 12th day of Python Practice
# Today, I will recap and practice what I have learned
# about Python so far and learn a little about boolean.
# In other words, I want to reinforce what I have learned so far, and
# add a little of what I learned today.

from datetime import date
from datetime import timedelta

class HealthBuilding:

    bloodsupply = False
    city = "Compsci City"
    currentDate = date.today()

    def __init__(self, newStatus, numNurses, numDoctors, numPatients):
        self.status = newStatus
        self.nurses = numNurses
        self.doctors = numDoctors 
        self.patients = numPatients
        currentDate = date.today()

    def prepareBlood(self):
        if self.bloodsupply is True:
            print("The blood for the blood transfusion is ready")
        else:
            print("There's not enough blood supply for a blood transfusion\nPlease request blood from the", self.city, "blood center")

    def requestBlood(self):
        estimatedDateofArrival = date.today() + timedelta(days = 3)
        if self.currentDate != estimatedDateofArrival:
            print("The request for blood from the blood center has been sent")
            print("The blood center said the blood will arrive in a few days.")
            print("Estimated Date of Arrival:", estimatedDateofArrival)
        else:
            self.bloodsupply = True
            print("The blood from the blood center has arrived!\nWe can perform blood transfusions now.")

    def incrementDay(self):
        self.currentDate =  self.currentDate + timedelta(days = 1)

    def printProperties(self):
        tempDict = {"City:" : self.city,
                       "Status:" : self.status,
                       "Number of Nurses:" : self.nurses,
                       "Number of Doctors:" : self.doctors,
                       "Number of Patients:" : self.patients}

        for i, j in tempDict.items():
            print(i, j)

    def patientLeaves(self):
        self.patients -= 1
        print("A patient has been discharged from the hospital!")

    def bloodtransfusion(self):
        if self.bloodsupply is True:
            print("The blood for the blood transfusion is ready.")
            print("The blood transfusion for the patient was successful!")
            print("The patient was happy about the operation!")
            self.patientLeaves()
        else:
            print("The hospital does not have adequate amounts of blood for a blood transfusion.")
            print("Please wait until the blood from the blood center arrives.")

    def printDate(self):
        print(self.currentDate)






exHealthBuilding = HealthBuilding(newStatus = "Full", numNurses = 25, numDoctors = 5, numPatients = 30)
exHealthBuilding.printProperties()
exHealthBuilding.requestBlood()
exHealthBuilding.incrementDay()
exHealthBuilding.incrementDay()
exHealthBuilding.incrementDay()
exHealthBuilding.requestBlood()
exHealthBuilding.bloodtransfusion()
exHealthBuilding.printDate()

# Things I learned when making this program
# 1. You cannot have more than one __init__.
# 1a. I was trying to make a default constructor and an overloaded constructor similar in Java.
# 2. When making keyword argument variables, the variables have to be the same name as the variable in the function parameter.
# 3. To increment a value like an int, use the "+=" operator.
# 4. To decrement a value, use the "-=" operator.

# Things to Remember and Recap:
# 1. Sets vs Lists vs Dictionary
# 2. __init__
# 3. Mutable objects such as lists, dictionaries, and sets are shared in all instances if it is declared as a class variable. i.e outside __init__

