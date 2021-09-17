## 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


expence = []
n = int(input("ENter the lenth of list "))
for i in range(0,n):
    b = int(input("ENter the expences "))
    expence.append(b)
    print(expence)
print("In Feb, how many dollars you spent extra compare to January? : ", expence[1]-expence[0])

expence.append(100)
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list :" , expence)

#You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expence[3] = expence[3] - 200
print("Expense after 200$ return in April:",expence)

