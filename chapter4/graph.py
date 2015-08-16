# Graph implementation 

class Vertex (object):
	def __init__ (self, label):
		self.label = label
		self.wasVisited = False

	def getLabel (self):
		return self.label

	def wasVisited (self):
		return self.wasVisited

class Edge (object):
	def __init__ (self, fromVertex, toVertex, weight=1):
		self.u = fromVertex
		self.v = toVertex
		self.weight = weight 

class Graph (object):
	def __init__ (self):
		self.vertices = []
		self.adjMatrix = []

	def addVertex (self, vertex):
		if not self.hasVertex(label):
			newVertex = Vertex(vertex)
			self.vertices.append(newVertex)

			numVert = len(self.vertices)
			for i in range (numVert - 1):
				self.adjMatrix[i].append(0)

			newRow = []
			for i in range (numVert):
				newRow.append(0)

			self.adjMatrix.append(newRow)

	def addUndirectedEdge (self, start, end, weight = 1):
		self.adjMatrix[start][end] = weight
		self.adjMatrix[end][start] = weight

	def addDirectedEdge (self, start, end, weight = 1):
		self.adjMatrix[start][end] = weight

	def getIndex (self, vert):
		for i in range (len(self.vertices)):
			if self.vertices[i].label == vert:
				return i

		return -1


















