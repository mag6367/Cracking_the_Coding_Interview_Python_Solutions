# question 1.5 from cracking the code interview 4th ed.
'''
Write a method to replace all spaces in a string with ‘%20’.
'''

# This solution uses the built in function str.replace()
def replace20 (string):
	# check the string is valid
	if not isinstance(string, str):
		return False

	return string.replace(" ", "%20")

# This solution uses recursion
def replace20Recurs (string):
	if len(string) == 0:
		return string
	elif string[0] == ' ':
		return '%20' + replace20Recurs(string[1:])
	else:
		return string[0] + replace20Recurs(string[1:])