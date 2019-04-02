#  File: ERsim.py
#  Description: LinkedList
#  Student's Name: Tyree Pearson
#  Student's UT EID: Tsp627
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 6-9-2017
#  Date Last Modified:6-10-2017


# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

class Node (object):
   
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this â€“ saves a lot
  
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER

       

class LinkedList:
  counter = 0
  def __init__(self):
      self.head = None
      
      
      
      
      
  def __str__ (self):
     # Return a string representation of data suitable for printing.
     #    Long lists (more than 10 elements long) should be neatly
     #    printed with 10 elements to a line, two spaces between
     #    elements
     
     current = self.head
     nodes = []
     c = ""
     while current != None: # when the last node is reached
             nodes.append(current.getData())
             current = current.getNext()
     #create a 10 string layout
     for i in range(len(nodes)):
         
         if i%10 == 0:
             c += '\n'
             c += str(nodes[i]) + " "
         else:
             c += str(nodes[i]) + "  "
             
     
     return c
 
  
  def addFirst (self, item): 
     # Add an item to the beginning of the list
     temp = Node(item)
     temp.setNext(self.head)
     self.head = temp
     

     
     
     

  def addLast (self, item): 
     # Add an item to the end of a list
     current = self.head
     temp = Node(item)
     prev = None
     while current != None:
         prev = current
         current = current.getNext()
      
     
            
     if prev == None:
         self.head = temp        
     else:
         prev.setNext(temp)
         

     

  def addInOrder (self, item): 
     # Insert an item into the proper place of an ordered list.
     # This assumes that the original list is already properly
     #    ordered.
     current = self.head
     previous = None
     stop = False
     while current!= None and not stop:
         if current.getData() > item:
             stop = True
         else:
              previous = current
              current = current.getNext()
     temp = Node(item)
     if previous == None:
             temp.setNext(self.head)
             self.head = temp
     else:
         temp.setNext(current)
         previous.setNext(temp)
  

  def getLength (self):
     # Return the number of items in the list
     current = self.head
     count = 0
     while current != None:
         count +=1
         current = current.getNext()
     return count
  
     
  def findUnordered (self, item): 
     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     
     current = self.head
     found = False
     while current != None and not found:
         if current.getData() == item:
             found = True
         else:
             current = current.getNext()
     return found
    
      
     

  def findOrdered (self, item): 
     # Search in an ordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     # This method MUST take advantage of the fact that the
     #    list is ordered to return quicker if the item is not
     #    in the list.
     current = self.head
     found = False
     stop = False
     while current != None and not found and not stop:
         if current.getData() == item:
             found = True
         else:
             if current.getData() > item:
                 stop = True
             else:
                 current = current.getNext()
     return found
  
  def delete (self, item):
     # Delete an item from an unordered list
     #    if found, return True; otherwise, return False
     current = self.head
     found = False
     previous = None
     #go through until item is found or end of list
     while current!=None and not found:
         if current.getData() == item:
             found = True
         else:
             previous = current
             current = current.getNext()
     #if item is found
     if found :
         #traversing through list while removing found
         if previous == None:
             self.head = current.getNext()
         else:
             previous.setNext(current.getNext())
     return found
 
         

  def copyList (self):
     current = self.head
     nodes = []
     newLink = LinkedList() # create the new obejct
     #append each item into list, but it is reveresed
     while current != None:
         nodes.append(current.getData())
         current = current.getNext()
     #Go through list from last to first creating a new LinkedList copy but start backwards
     for i in range(len(nodes)-1,-1,-1):
         newLink.addFirst(nodes[i])
     return newLink
         

  def reverseList (self): 
     # Return a new linked list that contains the elements of the
     #    original list in the reverse order.
     current = self.head
     nodes = []
     newLink = LinkedList() # create the new obejct
     
     #append each item into list, but it is reveresed
     while current != None:
         nodes.append(current.getData())
         current = current.getNext()
     #Go through list from last to first creating a new LinkedList copy that is reveresed  
     for i in range(0,len(nodes)):
         newLink.addFirst(nodes[i])
     return newLink
  
  def orderList (self): 
     # Return a new linked list that contains the elements of the
     #    original list arranged in ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list.
     current = self.head
     previous = None
     nodes= []
     newLink = LinkedList()
     while current != None:
        nodes.append(current.getData())
        current = current.getNext()
     for i in nodes:
         newLink.addInOrder(i)
     return newLink
 

  def isOrdered (self):
     # Return True if a list is ordered in ascending (alphabetical)
     #    order, or False otherwise
     current = self.head
     stop = False
     previous = current
     order = True
     #itterate through looking for higher values
     while current != None and not stop:
         if current.getData()<previous.getData():
             stop = True
             order = False
         
         current = current.getNext()

     return order
         
     

  def isEmpty (self): 
     # Return True if a list is empty, or False otherwise
     return self.head == None

  def mergeList (self, b): 
     # Return an ordered list whose elements consist of the 
     #    elements of two ordered lists combined.
     
     newLinks = self.copyList()
     currentB = b.head
     
     while currentB != None:
         newLinks.addInOrder(currentB.getData())
         currentB = currentB.getNext()
     return newLinks
     '''
     allnodes = []
     current = self.head
     currentB = b.head
     while current!= None and currentB != None:
        allnodes.append(current.getData())
        allnodes.append(currentB.getData())
        current = current.getNext()
        currentB = currentB.getNext()
     newLinks = LinkedList()
     for i in allnodes:
        newLinks.addInOrder(i)
     return newLinks
     '''

  def isEqual (self, b):
     # Test if two lists are equal, item by item, and return True.
     equal = True

     #Base is to test lengths
     if self.getLength() == b.getLength():
         current = self.head
         currentB = b.head
         
         #go through each node and compare
         while current!= None:
             if current.getData()!=currentB.getData():
                 equal = False
    
             #move on to next node
             current = current.getNext()
             currentB = currentB.getNext()
         
     else:
         equal = False
     return equal
     
         
     

  def removeDuplicates (self):
     # Remove all duplicates from a list, returning a new list.
     #    Do not change the order of the remaining elements.

     newList = self.copyList()
     current = newList.head
     previous = None
     nodes = [] # keep track of data
     #iterate through nodes
     while current != None:
         node = current.getData()
         #get each node into the list
         if node not in nodes:
             nodes.append(node)
             previous = current
             current = current.getNext()
         else:
             #if duplicate found
             #end of list, tranverse out the duplicates
             if previous == None:
                 newList.head = current.getNext()
                 previous = None
                 current = newList.head
             else:
                 previous.setNext(current.getNext())
                 current = previous.getNext()
     return newList
             
          
     
     ''' NOT IN ORDER
     current = self.head
     previous = None
     nodes = []
     newList = LinkedList()
     while current != None:
         nodes.append(current.getData())
         current = current.getNext()
     newNodes = set(nodes)
     newListNodes = list(newNodes)
     for i in newListNodes:
         newList.addInOrder(i)

     return newList
     '''
     





def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  ould see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
