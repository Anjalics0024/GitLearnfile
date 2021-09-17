numbers = []
n = int(input("ENter a Number : "))
for i in range(1,n+1):
        b=int(input("Enter element:"))
        numbers.append(b)
        print("Before reverseing : " ,numbers)
     
 
# Get list length
L = len(numbers)
 
# i goes from 0 to the middle
for i in range(int(L/2)):
    # Swap each number with the number in 
    # the mirror position for example first 
    # and last
    temp = numbers[i]
    numbers[i] = numbers[L-i-1]
    numbers[L-i-1] = temp
 
# At this point the list should be reversed
print("After reverseing : ", numbers)