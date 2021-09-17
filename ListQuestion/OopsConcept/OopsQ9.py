#Operator overloading : In this operator remain same and type of parameter are different and operand are different. it will behave like differenr way 

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __str__(self):
        return '{},{}'.format(self.m1,self.m2)
S1 = student(10,20)
S2 = student(30,50)

s3 = S1 + S2
print(s3.m2)

a = 9
print(a.__str__())

print(s3.__str__())  # behind the scene "s3" which is obejct it calling it method . behind the scnee it is calling __str__ method.
print(s3) 


