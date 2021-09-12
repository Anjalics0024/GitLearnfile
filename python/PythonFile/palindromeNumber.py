
'''
string = input("ENter a String :")

if (string== string[::-1]):
    print("ENter a string is palindrome  : ")

else:
    print("String is not palindrome : ")

'''

Num = int(input("ENter A Number"))
def reverseNumber(Num):
    sum= 0
    Temp = Num
    while Temp>0:
        remainder = Temp%10
        sum = sum*10 + remainder
        Temp//= 10
    return sum

if sum == Num:
    print("Enter a Number is palindrome")

else:
    print("Number is not palindrome")
rev_num = reverseNumber(Num)
print("Reverse of number is : ",rev_num)