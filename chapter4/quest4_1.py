# question 4.1 from cracking the code interview 4th ed.
# check the BTS implementation in the program here
'''
Implement a function to check if a tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance 
from the root by more than one.
'''

# just have to compare the minium and maximum paths of the tree
def isBalanced (root):

	return getMaxPath(root) - getMinPath(root) <= 1

# Gets the minimum path from a certain subtreee
def getMinPath (node):
	if node is None:
		return 0
	else:
		return min(node.leftChild, node.rightChild) + 1

# Gets the maximym path from a certain subtreee
def getMaxPath (node):
	if node is None:
		return 0
	else:
		return max(node.leftChild, node.rightChild) + 1