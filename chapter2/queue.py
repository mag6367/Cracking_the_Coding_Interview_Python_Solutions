class Queue (object):
	def __init__ (self):
		self.queue = []

	def enqueue (self, data):
		self.queue.append(data)

	def dequeue (self):
		if self.isEmpty():
			return 0

		return self.queue.pop(0)

	def isEmpty(self):
		return len(self.queue) == 0