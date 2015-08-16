# question 2.3 from cracking the code interview 4th ed.
# Look at LinkedList.py to understand the implementation of Linked List
'''
Implement an algorithm to delete a node in the middle of a single linked list, 
given only access to that node.
EXAMPLE
Input: the node ‘c’ from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
'''

# We simply need to copy the info from next node and delete the next node
def deleteMiddleNode (node):
	# Check if there are more nodes
	if not node.next:
		return False

	# This switches the nodes and the value of the node
	temp = node.next.next
	tempData = node.next.data
	node.next = temp
	node.data = tempData









