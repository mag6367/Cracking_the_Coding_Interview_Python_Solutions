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

	def removeDuplicate(self):
		values = []
		current = self.head
		values.append(current.data)
		previous = current
		current = current.next

		while current:
			if current.data in values:
				previous.next = current.next
			values.append(current.data)
			previous = current
			current = current.next


	def findLink (self, n):
		count = 1
		current = self.head
		previous = current

		# We will exit this while loop when we reach nth item or when there are no more links
		while current and count != n:
			count += 1
			previous = current
			current = current.next

		# Checks if n > # of linkes
		if count != n:
			return False

		# returns the link
		return current.data

	def deleteMiddleNode (self, node):
		# Check if there are more nodes
		if not node.next:
			return False

		# This switches the values
		temp = node.next.next
		temp1 = node.next.data
		node.next = temp
		node.data = temp1



	def __str__ (self):
		current = self.head
		values = []

		while current:
			values.append(current.data)
			current = current.next

		return '->'.join(str(x) for x in values)


from queue import Queue
from linkedList import LinkedList 


def addLinkedLists (LinkedList1, LinkedList2):
	# First we need to add the values to a queue in order to sum them
	queue1 = Queue()
	current1 = LinkedList1.head
	while current1:
		queue1.enqueue(current1.data)
		current1 = current1.next

	queue2 = Queue()
	current2 = LinkedList2.head
	while current2:
		queue2.enqueue(current2.data)
		current2 = current2.next


	# Now we need to add the numbers in reverse times 10^n
	sumValues = 0
	exp = 0
	while not queue1.isEmpty() or not queue2.isEmpty():
		sumValues += (queue1.dequeue() + queue2.dequeue()) * (10 ** exp)
		exp += 1
		print(sumValues)


	# The answer is actually sumValues reversed 
	finalAnswer = 0
	if sumValues < 0:  # because we are using string slice [::-1] operator to reverse, we need to check if negative
		sumValues = abs(sumValues)
		finalAnswer = int(str(sumValues)[::-1]) * -1
	else:
		finalAnswer = int(str(sumValues)[::-1])

	# Finally, we need to create a new linked List with the digits in order and return it
	finalList = LinkedList()

	while finalAnswer / 10 > 0:
		finalList.insertLast(finalAnswer % 10)
		finalAnswer = finalAnswer // 10

	return finalList

def main():
	l = LinkedList()

	l.insertLast(3)
	l.insertLast(1)
	l.insertLast(5)

	y = LinkedList()
	y.insertLast(5)
	y.insertLast(9)
	y.insertLast(2)

	print(l)
	print(y)
	print(addLinkedLists(l, y))

if __name__ == '__main__':
	main()

