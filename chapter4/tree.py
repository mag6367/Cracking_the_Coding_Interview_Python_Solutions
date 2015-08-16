class Node (object):
	def __init__ (self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

class BinaryTree (object):
	def __init__ (self):
		self.root = None

	def insert (self, data):
		newNode = Node(data)
		if self.root is None:
			self.root = newNode
			return 

		current = self.root
		previous = current 
		while current:
			previous = current 
			if current.data > data:
				current = current.leftChild
			else:
				current = current.rightChild

		current = newNode
		if previous.data > data:
			previous.leftChild = current
		else:
			previous.rightChild = current


	def inOrder (self, node):
		if node is not None:
			self.inOrder(node.leftChild)
			print(node.data)
			self.inOrder(node.rightChild)
















