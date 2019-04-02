#  File: MultiwayTree.py
#  Description: Check if trees are isomorphic
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 04/26/2017
#  Date Last Modified: 04/26/2017

class MultiwayTree:
	
	# initialize the tree with the given data and no children
	def __init__(self, pyTree):
		# the first element is the root data
		self.data = pyTree[0]
		self.children = []
		# the rest of the data is the children
		for child in pyTree[1]:
			childTree = MultiwayTree(child)
			self.children.append(childTree)
	
	# print out the tree in pre-order fashion
	def preOrder(self):
		st = str(self.data) + " "
		if len(self.children) > 0:
			for child in self.children:
				st += child.preOrder()
		return st
			
	
	# return True if the tree "self" has the same structure as the tree "other"
	# "False" otherwise.
	def isIsomorphicTo(self, other):
		isIsomorphic = True
		
		# check if the lengths of the children is the same, if not, trees are not
		# isomporphic
		if len(self.children) != len(other.children):
			return False
		
		# check that each child is an isomorphic tree
		if len(self.children) > 0:
			for i in range(len(self.children)):
				isIsomorphic = self.children[i].isIsomorphicTo(other.children[i])
		
		return isIsomorphic

def main():
	
	infile = open("MultiwayTreeInput.txt", "r")
	
	# input all of the tress
	unformatedTrees = []
	for line in infile:
		unformatedTrees.append(eval(line))
	infile.close()
	
	for i in range(0, len(unformatedTrees), 2):
		firstTree = unformatedTrees[i]
		secondTree = unformatedTrees[i+1]
		
		print()
		
		# print out each tree, convert it to a mutliway tree,
		# then print out the preorder version
		print("Tree %d:" % (i+1), firstTree); firstTree = MultiwayTree(firstTree)
		print("Tree %d preorder:" % (i+1), firstTree.preOrder())
		
		print()
		
		print("Tree %d:" % (i+2), secondTree); secondTree = MultiwayTree(secondTree)
		print("Tree %d preorder:" % (i+2), secondTree.preOrder())
		
		print()
		
		# test if the trees are isomorphic
		if firstTree.isIsomorphicTo(secondTree):
			print("Tree %d is isomorphic to Tree %d" % (i+1, i+2))
		else:
			print("Tree %d is not isomorphic to Tree %d" % (i+1, i+2))

		
		
		print()
	
if __name__ == "__main__":
	main()
