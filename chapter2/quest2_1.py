# question 2.1 from cracking the code interview 4th ed.
# Look at LinkedList.py to understand the implementation of Linked List
'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP:
How would you solve this problem if a temporary buffer is not allowed?
'''

# With temporary buffer
def removeDuplicate(LinkedList):
	# values will store the data
	values = []
	current = linkedList.head
	values.append(current.data)

	# we need to keep track of previous Link and move the Link up
	previous = current
	current = current.next

	while current:
		if current.data in values:
			previous.next = current.next
		else:
			values.append(current.data)
			previous = current
			current = current.next

	return current


# without temp buffer

def removeDuplicate2 (LinkedList):
	#TODO: Implement me
	pass
