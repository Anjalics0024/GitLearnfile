class computer: #class declaration

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("I am init method")
        pass

    def config(self): #method of class
        print("config is : ", self.cpu,self.ram)

comp1 = computer('i5','7GB') #one class can have different object
comp2 = computer('i7','16GB')
computer.config(comp1)  # Class is using to call method 
comp2.config()     # Another way  to call bject . In this object itself using to call method "Config"
comp1.config() # here we ar enot passing two argument here are 3 argument by default comp2 is getting passed
