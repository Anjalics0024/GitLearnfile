a=[]
c = []
temp = 0
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
print("Before swapping list is : ",a)   
F = print("First Element:",a[0])
L = print("Last Element:",a[-1])

temp = a[0]
a[0] = a[-1]
a[-1] = temp
print("After swapping list is " , a)
