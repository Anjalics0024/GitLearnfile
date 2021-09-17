#Python program to find smallest number in a list
#using sort method
a =[]
c = []
n = int(input("ENter a Number : "))
def smallest():
    for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
        print(a)
        
    
    return a
smallest()
a = []
n = int(input("ENter a Number : "))
for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
        print(a)

a.sort()
print("smallest number is : " , a[:1])

#Using without sort function
a = []
n = int(input("ENter a Number : "))
for i in range(1,n+1):
    
    b=int(input("Enter element:"))
    a.append(b)
    print(a)   
min = a[0]
for i in range(len(a)):
    if a[i]< min:
        min = a[i]
print("smallest number is : ",min)




