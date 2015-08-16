# question 4.2 from cracking the code interview 4th ed.
'''
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''

# We use the adjecancy matrix on our graph class 
# for this solution make sense please look at graph.py

from graph import Graph 

def hasRoute (graph, vert1, vert2):
	# get the index
	index1 = graph.getIndex(vert1)
	index2 = graph.getIndex(vert2)

	return graph.adjMatrix[index1][index2] == 1 or graph.adjMatrix[index2][index1] == 1
