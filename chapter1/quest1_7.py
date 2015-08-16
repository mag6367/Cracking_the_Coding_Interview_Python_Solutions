# question 1.7 from cracking the code interview 4th ed.
'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
'''

# We use a hash table to store both row and col then we set them to zero

def setMatZero (matrix):
	# check is is a valid matrix
	if not isinstance(matrix, list):
		return False

	# hash for cols and rows
	cols_rows = {}
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			if matrix[i][j] == 0:
				cols_rows[i] = j

	# now we change the values
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			if i in cols_rows or j in cols_rows.values():
				matrix[i][j] = 0

	
