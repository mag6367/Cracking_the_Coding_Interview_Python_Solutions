# question 4.4 from cracking the code interview 4th ed
'''
Given a binary search tree, design an algorithm which creates a linked list of all 
the nodes at each depth (eg, if you have a tree with depth D, you’ll have D linked lists).
'''
from tree import BinaryTree 
from linkedList import LinkedList

# the function will take a binary search tree as a parameter
def linkedTree (tree):
	root = tree.root

	height = getHeight(root)

	# create height linked lists putting them inside a list
	linkedArray = []
	for i in range (height):
		linkedArray.append(LinkedList())

	# This will create the linked lists inside linkedArray
	createLinkedTree(root, 0, linkedArray)

	return linkedArray

# here we create the linked lists recursively 
def createLinkedTree (node, level, array):
	if node is not None:
		array[level].insertFirst(node.data)
		createLinkedTree(node.leftChild, level+1, array)
		createLinkedTree(node.rightChild, level+1, array)

def getHeight (node):
	if node is None:
		return 0
	else:
		return max(getHeight(node.leftChild), getHeight(node.rightChild)) + 1
