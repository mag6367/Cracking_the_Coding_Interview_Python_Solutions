# question 3.2 from cracking the code interview 4th ed.
'''
How would you design a stack which, in addition to push and pop, 
also has a function min which returns the minimum element? Push, 
pop and min should all operate in O(1) time.
'''

# What we can do is simply keep track of the minimum number in the class
class Stack (object):
	def __init__ (self):
		self.stack []
		self.min = None

	# When we push a new item, we keep track of the min
	def push (self, data):
		if self.min is None:
			self.min = data
		self.min = min(data, self.min)

		self.stack.append(data)

	# This operation is O(1)
	def getMin (self):
		return self.min

	def pop (self):
		return self.stack.pop()

