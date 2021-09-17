#Inheritance 

class A:
    def feature1(self):
        print("I am feture1 method")
    
    def feature2(self):
        print("I am feture2 method")



class B(A):

    def feature3(self):
        print("I am feture3 method")
    
    def feature4():
        print("I am feture4 method")

#multi level inheritance
class C(B):
    def feature5(self):
        print("I am feature 5 ")


#multiple inheritance
class C(B,A):
    def feature5(self):
        print("I am feature 5 ")



ob = A()
ob2 = B()
ob3 = C()

#SIngle level inheritance
#ob.feature1()
#ob.feature2()

ob2.feature3()


#multiple level inheritance
ob3.feature5()



