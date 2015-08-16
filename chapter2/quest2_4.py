# question 2.4 from cracking the code interview 4th ed.
# Look at LinkedList.py to understand the implementation of Linked List
'''
You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1’s digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
'''

# This is a really interesting problem that takes numerous steps to solve
# We will need to implement a Queue data structure because of the way the numbers are arranged in LL
# stacks module is in this directory 
from stacks import Stack
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



