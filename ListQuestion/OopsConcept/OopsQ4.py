#Types of Method, 1. Instance method 2. Class method 3. Static Method

class student:
    school = "Army School Nasirabad"   #class vairable
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #instance method , In instance we have two type 1. Accessor Method (Just to fecth the value of its Method) 2.Mutator Method(If you want ti modify the value of method then we use mutator )
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):  #this will set the value work as getter or Accessor
        return self.m1

    def set_m1(self,value):  #this will set the value work as Setter also mutator 
        self.m1 = value
    @classmethod
    def info(cls):  #here we are using "cls" as working with class variable , # class method
        return cls.school

    @staticmethod
    def static():  #here we are using static method. If you want to do something extra apart from instance and class method then we use static
        print("This is static Method ")

stu1 = student(10,20,30)
stu2 = student(40,50,60)
print(stu1.m1,stu2.m2,stu1.m3)
print(stu1.m1,stu2.m2,stu1.m3)
print(stu1.avg())
print(student.info())

print(stu2.static())