# question 3.6 from cracking the code interview 4th ed.
'''
Write a program to sort a stack in ascending order. You should not make any assumptions 
about how the stack is implemented. The following are the only functions that should 
be used to write this program: push | pop | peek | isEmpty.
'''

from stack import Stack 

# We can use sort a stack using another stack

def sortStack (stack):
	newStack = Stack()
	
	while not stack.isEmpty():
		temp = stack.pop()
		while not newStack.isEmpty() and newStack.peek() > temp:
			stack.push(newStack.pop())
		newStack.push(temp)

	return newStack




