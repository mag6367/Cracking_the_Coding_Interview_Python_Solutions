# question 1.7 from cracking the code interview 4th ed.
'''
Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
(i.e., “waterbottle” is a rotation of “erbottlewat”).
'''

# 
def isRotation (str1, str2):
	# check is strings are valid
	if (not isinstance(str1, str) or not isinstance(str2, str)) or len(str1) != len(str2):
		return False

	