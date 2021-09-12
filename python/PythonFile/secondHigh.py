a=[]
c = []
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
    c = a.sort()
    print(c)
print(a)
    
print("Second largest element is:",a[n-2])