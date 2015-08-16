# question 1.1 from cracking the code interview 4th ed.
'''
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?
'''

# Create a set and compare the lengths (sets remove any duplicates)
def uniqueChars (string):
	# check the string is valid
	if not isinstance(string, str):
		return False

	compareStr = set(string)
	return len(compareStr) == len(string)

# Solution with no data structure 
def uniqueChars2 (string):
	# check the string is valid
	if not isinstance(string, str):
		return False

	# the two loops we will compare every single char in the string
	for i in range (len(string) - 1):
		for j in range (i + 1, len(string)):
			if string[i] == string[j]:
				return True

	return False
