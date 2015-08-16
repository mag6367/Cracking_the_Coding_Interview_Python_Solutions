# question 1.3 from cracking the code interview 4th ed.
'''
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. 
NOTE: One or two additional variables are fine. An extra copy of the array is not.
'''

# The solution will append to a new list and return it a string of it
def removeUniqueChar (string):
	# check the string is valid
	if not isinstance(string, str):
		return False

	answer = []
	for ch in string:
		if ch not in answer:
			answer.append(ch)

	# this returns the the list in string form
	return ''.join(answer)
