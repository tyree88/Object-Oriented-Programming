
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 11/25/2016
#  Date Last Modified: 11/26/2016
class BinaryTree (object):

	def __init__(self,initVal=None):
		self.data = initVal
		self.left = None
		self.right = None
		## Initializes the tree for a list input
		if type(initVal) == list:
			self.createTree(initVal)

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.left = self.left
			self.left = t

	def insertRight(self,newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.right = self.right
			self.right = t

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def setRootVal(self,value):
		self.data = value

	def getRootVal(self):
		return self.data

	def createTree (self, expr):
		"""Generates the tree by destroying expr.  every left parenthesis
		essentially makes us recur a layer deeper until we find numbers. This
		method strongly abuses the fact that we know the input will be valid"""

		token = expr.pop(0)
		if token == '(':
			self.left = BinaryTree(expr)
			## After all left nodes have been popped, we know the current
			## node must be an operator, by nature of input.  Set current
			## node to the operator and set the right node afterwards
			self.data = expr.pop(0)
			self.right = BinaryTree(expr)
			## Simply removes right parentheses
			expr.pop(0)
		## Base Case - abuse
		else:
			self.data = self.convert(token)

	def evaluate (self):
		"""InOrder traversal to generate a total"""
		if self.isop(self.data):
			return self.op(self.left.evaluate(), self.right.evaluate())
		else:
			return self.data

	def convert(self, token):
		"""Returns the float/int of an input"""
		## Simple way to check if token is a float type
		if token.find('.') != -1:
			return float(token)
		else:
			return int(token)

	def isop(self, token):
		"""Just a shortcut to return whether a token is an operator"""
		return token in ['+', '-', '*', '/']

	def op(self, x, y):
		"""A somewhat intuitive method to handle basic arithmetic expressions
		"""
		operator = self.data # Only op nodes are passed in anyway
		return {
        '+' : (lambda x,y: x+y),
        '-' : (lambda x,y: x-y),
        '*' : (lambda x,y: x*y),
        '/' : (lambda x,y: float(x/y))
        }[operator](x, y)

	def preOrder (self):
		"""Traverses the tree in preOrder fashion to generate prefix notation
		"""
		if type(self.data) == int or type(self.data) == float:
			return [str(self.data)]
		else:
			return [self.data] + self.left.preOrder() + self.right.preOrder()


	def postOrder (self):
		"""Traverses the tree in postOrder fashion to generate postfix notation
		"""
		if type(self.data) == int or type(self.data) == float:
			return [str(self.data)]
		else:
			return self.left.postOrder() + self.right.postOrder() + [self.data]

def main():
	""" Main function"""
	## Grabs text file input
	f = open('treedata.txt', 'r')
	ln = f.readline()

	## Executes as long as ln is not ''
	while ln:
		## Grabs tokens and makes a tree using a list input
		tokens = ln.split()
		tree = BinaryTree(tokens)
		## Prints all required outputs by using different traversal types
		print("Infix expression: {}".format(ln))
		print("Value:   {}".format(tree.evaluate()))
		print("Prefix expression: {}".format(' '.join(tree.preOrder())))
		print("Postfix expression: {}\n" .format(' '.join(tree.postOrder())))
		## Re-sets ln
		ln = f.readline()

if __name__ == '__main__' : main()
