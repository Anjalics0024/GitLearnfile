'''

def checkString(string):
    flag_l = False
    flag_N = False

    for i in string:
        if i.isdigit():
            flag_l = True
        if i.isalnum():
            flag_N = True

    return flag_N and flag_l
string = input("Enter a string : ")
print(string)
'''

def checkString(str):
	
	# intializing flag variable
	flag_l = False
	flag_n = False
	
	# checking for letter and numbers in
	# given string
	for i in str:
		
		# if string has letter
		if i.isalpha():
			flag_l = True

		# if string has number
		if i.isdigit():
			flag_n = True
	
	# returning and of flag
	# for checking required condition
	return flag_l and flag_n


# driver code
str = input("Enter a string : ")
print(checkString(str))
print(checkString(str))
