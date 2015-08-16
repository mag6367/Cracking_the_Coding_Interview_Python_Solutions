# This file will implement a Linked List Data Structure

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.next = None

class LinkedList (object):
	def __init__ (self):
		self.head = None

	def insertFirst (self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def insertLast (self, data):
		newNode = Node(data)
		current = self.head

		if current is None:
			self.head = newNode
			return 

		while current.next:
			current = current.next

		current.next = newNode

	def deleteNode (self, data):
		current = self.head
		previous = self.head

		if current is None:
			return False

		while current.data != data:
			previous = current
			current = current.next
			if current is None:
				return False

		if current is self.head:
			self.head = self.head.next
		else:
			previous.next = current.next

		return current 


	def __str__ (self):
		current = self.head
		values = []

		while current:
			values.append(current.data)
			current = current.next

		return '->'.join(str(x) for x in values)



