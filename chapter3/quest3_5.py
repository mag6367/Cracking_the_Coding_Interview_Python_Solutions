# question 3.5 from cracking the code interview 4th ed.
'''
Implement a MyQueue class which implements a queue using two stacks.
'''

from stack import Stack


class myQueue (object):
	def __init__ (self):
		self.stack1 = []
		self.stack2 = []

	# enqueue into stack 1
	def enqueue (self, data):
		self.stack1.append(data)

	# pop all values from stack1 to stack 2
	def dequeue (self):
		size1, size2 = self.size()
		if size2 != 0:
			return self.stack2.pop()

		while size1 != 0:
			self.stack2.append(self.stack1.pop())
			size1, size2 = self.size()

		return self.stack2.pop()

	# similar to dequeue, pop all stack 1 values into stack 2, return first item
	def peek (self):
		size1, size2 = self.size()
		if size2 != 0:
			return self.stack2[-1]

		while size1 != 0:
			self.stack2.append(self.stack1.pop())
			size1, size2 = self.size()

		return self.stack2[-1]


    # Returs a tuple the lengths of stack 1 and 2 respectively 
	def size (self):
		return len(self.stack1), len(self.stack2)




