

#Constructor in Inheritance How it behave 
#How to use super() keyword in inheritance 
# MRO - Method resolution order

class A:

    def __init__(self):
        print("I am init A Class")

    def feature1(self):
        print("I am feture1 method")
    
    def feature2(self):
        print("I am feture2 method")

class B(A):

    
    def __init__(self):
        super().__init__()   # By using this it will call init of class sub class
        print("I am init B Class")
        

    def feature3(self):
        print("I am feture3 method")
    
    def feature4(self):
        print("I am feture4 method")




#multiple inheritance
class C(B,A):

    def __init__(self):
        super().__init__()   #It will give A init first from left to right . This is called MRO "Method resolution Oredr " . Means when we have muptiple inheritance then it will prefer left one first , it go from left to right
        print("I am init of C")
    def feature5(self):
        print("I am feature 5 ")

    
    def feat(self):
        super().feature2()

#ob2 = B()  # it will give init of B only 
#if we want init of class A also > how can be do that ? #  using Super() method 

ob2 = C()

ob2.feat()






