#  File: Expression Tree
#  Description: Evaluate an expression with a tree 
#  Student's Name: Tyree Pearson
#  Student's UT EID: Tsp627
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 8-7-2017
#  Date Last Modified:8-7-2017




class MultiwayTree:
    #given "pyTree", a python representation of a tree,
    #create a node and pointer representation of that tree
    def __init__ (self,pyTree): 
        self.data = pyTree[0]
        self.children = []
        for child in pyTree[1]:
            childTree = MultiwayTree(child)
            self.children.append(childTree)

    #Print out the node and pointer represtnation of a tree using preorder
    def preOrder(self):
        node = self.data
        s = " "+str(node)
        if len(self.children)>0:
            for child in self.children:
                s += str(child.preOrder())
                
        return s
        
        

    # Return True if the tree "self" has the same structure as the
    #tree "other", "False" otherwise
    def isIsomorphicTo(self,other):
        isIsomorphic = True
        #Check Length
        if len(self.children) != len(other.children):
            return False

        if len(self.children) > 0:
            for i in range(len(self.children)):
                isIsomorphic = self.children[i].isIsomorphicTo(other.children[i])
        return isIsomorphic




def main():
    infile = open("MultiwayTreeInput.txt","r")
    #Create Tree 
    tree = []
    for line in infile:
        tree.append(eval(line))
    #print(tree)
    
    for i in range(0, len(tree),2):
        #create the multiway tree for preorder version 
        tree1 = MultiwayTree(tree[i])
        
        print("Tree ",i+1,":", tree[i])
        print("Tree ",i+1,"preorder:",  tree1.preOrder())
        print()
        #create second multiway tree 
        tree2 = MultiwayTree(tree[i+1])

        print("Tree ",i+2,":",tree[i+1])
        print("Tree ", i+2, "preorder:", tree2.preOrder())
        print()
        #Check if the tree is Isomorphic 
        if tree1.isIsomorphicTo(tree2):
            print("Tree", i+1," is Isomorphic to Tree", i+2)
        else:
            print("Tree", i+1," is not Isomorphic to Tree", i+2)
    
        print()

    



main()
        
