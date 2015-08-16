# question 1.2 from cracking the code interview 4th ed.
''' 
Write code to reverse a C-Style String. 
(C-String means that “abcd” is represented as five characters, including the null character)
'''

'''
I will show how to reverse a string in Python two ways.
We will not care about the c-style String
'''

# Use the slice operator [::-1]
def reverseString (string):
	# check the string is valid
	if not isinstance(string, str):
		return False

	# the slice operator [::-1] reverses a string
	return string[::-1]

# Solution using stack data structure 
def reverseStringStack (string):
	# check the string is valid
	if not isinstance(string, str):
		return False

	# first convert the string into a list
	stack = list(string)

	# now we pop the stack and append to new string until stack is empty
	newString = "" 
	while len(stack) != 0:
		newString += stack.pop()

	return newString

