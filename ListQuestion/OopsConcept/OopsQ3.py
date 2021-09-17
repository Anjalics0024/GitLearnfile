#Type of Variable 
class Car:

    wheel = 5 # variable that are definec inside class are class variable and class vairable are also called as static vairable.
    def __init__(self):  # varible thar are defince inside __init__ are instance variable 
        self.name = "BMW"
        self.milage = 10
C1 = Car()
C2 = Car()
C2.milage = 8
print(C1.name, C1.milage,C1.wheel)
print(C2.name, C2.milage)