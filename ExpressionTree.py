#  File: Expression Tree
#  Description: Evaluate an expression with a tree 
#  Student's Name: Tyree Pearson
#  Student's UT EID: Tsp627
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 8-2-2017
#  Date Last Modified:8-2-2017




class BinaryTree:
     
     
    def __init__ (self, initVal):
       self.data = initVal
       self.left = None
       self.right = None
       if type(initVal) ==list:
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
        #Remove parenthesis
        token = expr.pop(0)
        #start the ordering of Arithmetic Operators
        if token == '(':
            self.left = BinaryTree(expr)
            
            self.data = expr.pop(0)
            self.right = BinaryTree(expr)
            #Removes right expression 
            expr.pop(0)
        else:
            #evaluate data 
            self.data = eval(token)
            

            
    #PREORDER
    def preOrder(self):
        space = " "
        #MAKE SURE IT IS NUMBER
        if type(self.data) == int or type(self.data) == float:
            return str(self.data) + space
        else:
            return space + self.data + space + self.left.preOrder() + self.right.preOrder() 

    #POST ORDER
    def postOrder (self):
        space = " "
        #MAKE SURE IT IS NUMBER
        if type(self.data) == int or type(self.data) == float:
            return str(self.data) + space
        else:
            return self.left.postOrder() + self.right.postOrder() + space + self.data + space 


    def evaluate(self):
        operators = ['+','-','*','/']
        #IF OPERATOR
        if self.data in operators:
            if self.getRootVal() == '+':
                return (self.left.evaluate() + self.right.evaluate())
            elif self.getRootVal() == '-':
                return (self.left.evaluate() - self.right.evaluate())
            elif self.getRootVal() == '*':
                return (self.left.evaluate() * self.right.evaluate())
            else:
                return (float(self.left.evaluate() / self.right.evaluate()))
        
        else:
            return self.data
        


def main():

    #Get File
    infile = open("treedata.txt", "r")
    line = infile.readline()
    
    while line:
        token = line.split()
        tree = BinaryTree(token)        
        print("Infix expression:   ", line)
        print()
        print("   Value   ",tree.evaluate())
        print("   Prefix expression: ", tree.preOrder())
        print("   Postfix expression: ", tree.postOrder())
        
        print()
        
        #Get next line
        line = infile.readline()



main()



    
    
    

