#Method Overloading :1. Compile time polymorphisam 2.Same method name but different argument 3.No need of more than one class

#method(a,b)
#method(a,b,c)

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def add(self,a= None, b=None, c=None):
        s = a+b+c
        return s

s1 = student(66,100)
print(s1.add(2,9,10))

#Method Overriding 1.Example of compile time popymorphism 2.Atleast two class are requied 3.Same method and same argument

class A:

	def fun1(self):
		print('feature_1 of class A')
		
	def fun2(self):
		print('feature_2 of class A')
	

class B(A):
	
	# Modified function that is
	# already exist in class A
	def fun1(self):
		print('Modified feature_1 of class A by class B')
		
	def fun3(self):
		print('feature_3 of class B')
		

# Create instance
obj = B()
	
# Call the override function
obj.fun1()

        