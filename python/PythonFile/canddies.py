total_canddies = int(input("ENter Total candies in jar "))
candies_remove = int(input("ENter Number of candies you want "))

if candies_remove in range(1,6):
    print("Number of candies removed are : ", candies_remove)
    print("Number of candies left are : ", total_canddies - candies_remove)

else:
	print("Invalid Input")
	print('No. of Candies Left:',total_canddies)
