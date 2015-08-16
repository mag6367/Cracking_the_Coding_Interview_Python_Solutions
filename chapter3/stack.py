# Stack implementation

class Stack (object):
	def __init__ (self):
		self.stack = []

	def push (self, data):
		self.stack.append(data)

	def peek (self):
		if self.isEmpty():
			return None
		return self.stack[-1]

	def pop (self):
		if self.isEmpty():
			return None	
		return self.stack.pop()

	def isEmpty (self):
		return len(self.stack) == 0

	def __str__ (self):
		return ' '.join(str(x) for x in self.stack)

