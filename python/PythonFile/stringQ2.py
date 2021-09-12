from typing import Counter


'''

def string(filename , letter:
    file = open('file.txt',"r")
    text = file.read()
    count = 0
    for char in text:
        if char == letter:
            count+=1

        return Count

print(string('file.txt',"r"))



'''

# Program to get letter count in a text file

# explit function to return the letter count
def letterFrequency(fileName, letter):
	# open file in read mode
	file = open(fileName, "r")

	# store content of the file in a variable
	text = file.read()

	# declare count variable
	count = 0

	# iterate through each character
	for char in text:

		# compare each character with
		# the given letter
		if char == letter:
			count += 1

	# return letter count
	return count


# call function and display the letter count
print(letterFrequency('file.txt', 'g'))
