Num = int(input("Enter a Number"))
def fibanocci(Num):
    fib = 2
    if Num<0:
        print("result are invalid")

    elif Num==1:
        return 1

    elif Num>1:
        fib = fibanocci(Num-1)+fibanocci(Num-2)

    return fib
        
result = fibanocci(Num)
print("series is : ",result)