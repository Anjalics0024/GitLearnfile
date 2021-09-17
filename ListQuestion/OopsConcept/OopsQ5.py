#Inner Class : Class inside class

class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()  

    def show(self):
        print(self.name,self.rollno)
        self.lap1.show()


    class laptop:  #inner class

        def __init__(self):
            self.brand = "HP"
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)
            



S1 = student('Anjali',24)
S2 = student('Akchat',14)
S1.show()
lap1 = student.laptop()   #We can create object of inner class inside outer class OR we can create obejct of inner class outside the outer class provided you should use outer class name to call . Likewise we have use student.ineerclass name
