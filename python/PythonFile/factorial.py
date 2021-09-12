Num = int(input("Enter a Number   :"))
'''
def factorial(Num):
    fact = 1
    if Num==1:
        return 1

    else:
        fact = Num*factorial(Num-1)
        return fact

    return fact
'''

def factorial(Num):
    fact = 1
    while Num>1:
        fact = fact*Num
        Num-=1
    return fact
    

facto_rial = factorial(Num)
print("Factorila of number is: ",facto_rial)

  

