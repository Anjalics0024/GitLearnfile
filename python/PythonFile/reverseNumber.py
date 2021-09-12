Num = int(input("ENter A Number"))

def reverseNumber(Num):
    sum= 0
    while Num>0:
        remainder = Num%10
        sum = sum*10 + remainder
        Num//= 10
        print(Num)
    return sum




rev_num = reverseNumber(Num)
print("Reverse of number is : ",rev_num)