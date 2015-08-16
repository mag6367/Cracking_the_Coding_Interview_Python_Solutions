# question 3.3 from cracking the code interview 4th ed.
'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks,
and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() 
should behave identically to a single stack (that is, pop() should return the same values as it would if there 
were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''


# In python, lists would never care about how much we insert in them, so we'll make an arbitrary max number - 25
# We will use a 2D List to implement this 

class SetOfStacks (object):
	def __init__ (self):
		self.stack = []

		# max number of each stack is 25
		for i in range (25):
			# Make 10 stacks
			temp = [None] * 10
			self.stack.append(temp)

		self.rank = 0
		self.table = -1

	def push (self, data):
		index = self.getIndex()
		if index == 0:
			self.table += 1

		self.stack[table][index] = data
		self.rank += 1

	def getIndex (self):
		return self.rank % 25


	def pop (self):
		index = self.getIndex()
		poppedVal = self.stack[self.table][index]

		self.stack[self.table][self.rank] = None
		if self.rank % 25 == 0:
			self.table -= 1
		self.rank -= 1

		return poppedVal







