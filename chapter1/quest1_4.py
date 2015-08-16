# question 1.4 from cracking the code interview 4th ed.
'''
Write a method to decide if two strings are anagrams or not.
'''

# if we sort the two string, they should be the same
def areAnagram (str1, str2):
	# check is strings are valid
	if not isinstance(str1, str) or not isinstance(str2, str):
		return False

	# first we convert the two strings into lists and sort them
	newStr1 = list(str1)
	newStr1.sort()

	newStr2 = list(str2)
	newStr2.sort()

	# if they are anagrams, the lists should be identical
	return newStr1 == newStr2


