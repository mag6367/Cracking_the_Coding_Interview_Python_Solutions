# question 4.3 from cracking the code interview 4th ed
'''
Given a sorted (increasing order) array, write an algorithm to create a binary tree 
with minimal height.
'''
from tree import BinaryTree, Node
# this is actually really easy. All we need is to insert the middle value as the root

def minHeightTree (array):
	mid = len(array) // 2

	tree = BinaryTree()

	root = Node(array.pop(mid))
	self.root = root

	for nums in array:
		tree.insert(nums)



