Num = int(input("ENter A Number"))

def armstrongNumber(Num):
    sum= 0
    x = len(str(Num))
    while Num>0:
        remainder = Num%10
        sum = sum + remainder**x
        Num//= 10
    return sum
if sum==Num:
    print("enter number is Armstrong  :", Num)

else:
    print("No : ")

rev_num = armstrongNumber(Num)
print("armstrong Number is : ",rev_num)