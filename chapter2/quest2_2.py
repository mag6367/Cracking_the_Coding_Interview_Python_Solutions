# question 2.2 from cracking the code interview 4th ed.
# Look at LinkedList.py to understand the implementation of Linked List
'''
Implement an algorithm to find the nth to last element of a singly linked list.
'''

# We create a temporary count and we increment it each time we go to next
# If n is bigger than the # of nodes, return False
def findLink (LinkedList, n):
	count = 1
	current = LinkedList.head
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
	return current



