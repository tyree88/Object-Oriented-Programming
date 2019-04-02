
#  File: LinkedLists.py
#  Description: Implement a single class that combines Unorder and Ordered LinkedList capabilities
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 03/11/2017
#  Date Last Modified: 03/17/2017

class Node (object):
    '''
    Taken from class notes
    '''
    def __init__(self,initdata):
        self.data = initdata
        self.next = None            # always do this – saves a lot
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
    
    def __init__ (self):
        self.head = None

    def __str__ (self):
        # Return a string representation of data suitable for printing.
        #    Long lists (more than 10 elements long) should be neatly
        #    printed with 10 elements to a line, two spaces between
        #    elements
        current = self.head
        data = []
        
        # itterate through the list and pull out all of the data
        while current != None:
            data.append(current.getData())
            current = current.getNext()
            

        # print all of the nodes two spaces apart, ten to a line
        str = ""
        for i in range(len(data)):
            if(i % 10):
                str += data[i] + "  "
            else:
                str += "\n"
                str += data[i] + "  "
        str += "\n"     
        return str
    
    def addFirst (self, item):
        # Add an item to the beginning of the list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def addLast (self, item): 
        # Add an item to the end of a list
        temp = Node(item)
        current = self.head
        previous = None
        
        while current != None:
            previous = current
            current = current.getNext()
            
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def addInOrder (self, item):
        # Insert an item into the proper place of an ordered list.
        current = self.head
        previous = None
        stop = False

        # traverse until a later letter or the end is found
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        # if this is the first item
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        # if not the first item
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getLength (self):
        # Return the number of items in the list
        current = self.head
        count = 0

        # traverse through the list and count how many items there are
        while current != None:
            count += 1
            current = current.getNext()

        # return the count
        return count

    def findUnordered (self, item): 
        # Search in an unordered list
        current = self.head
        found = False

        # search until either the item is found or the end of the list is reached
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        # True if found, False if not
        return found
    
    def findOrdered (self, item): 
        # Search in an ordered list
        current = self.head
        found = False
        stop = False
        
        # search until the item is found or the boundary is passed, or the end is reached
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        # True if found, False if not
        return found


    def delete (self, item):
        # Delete an item from an unordered list
        current = self.head
        previous = None
        found = False

        # search until the item is found or until the end of the list is reached
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # if the item was found, delete it
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            
        # True if found, False if not
        return found
     
    def copyList (self):
        # Return a new linked list that's a copy of the original,
        #    made up of copies of the original elements
        newList = LinkedList()
        current = self.head
        data = []
        
        # go through the list and add each item to the new list
        while current != None:
            data.append(current.getData())
            current = current.getNext()
        # add the items in reverse order they came out, like a stack
        for i in range(len(data) - 1, -1, -1):
            newList.addFirst(data[i])
        
        # return the list
        return newList

    def reverseList (self): 
        # Return a new linked list that contains the elements of the
        #    original list in the reverse order.
        current = self.head
        newList = LinkedList()
        data = []
        
        # itterate through the list and get all of the data
        while current != None:
            data.append(current.getData())
            current = current.getNext()
            
        # add the data back, it'll be in reverse order
        for d in data:
            newList.addFirst(d)
            
        # return the reversed list
        return newList
    
    def orderList (self): 
        # Return a new linked list that contains the elements of the
        #    original list arranged in ascending (alphabetical) order.
        current = self.head
        newList = LinkedList()
        data = []
        
        # itterate through the list and get all of the data
        while current != None:
            data.append(current.getData())
            current = current.getNext()
            
        # add the data back, it'll be in reverse order
        for d in data:
            newList.addInOrder(d)
            
        # return the sorted list
        return newList

    def isOrdered (self):
        # Return True if a list is ordered in ascending (alphabetical)
        #    order, or False otherwise
        current = self.head
        previous = current
        stop = False
        ordered = True
        
        # itterate through the list and find if any preceding values are larger than the proceeding
        while current != None and not stop:
            if previous.getData() > current.getData():
                stop = True
                ordered = False
            current = current.getNext()
        
        # return True if ordered, false otherwise
        return ordered

    def isEmpty (self): 
        # Return True if a list is empty, or False otherwise
        return self.head == None

    def mergeList (self, b): 
        # Return an ordered list whose elements consist of the 
        #    elements of two ordered lists combined.
       
        # copy the first list
        newList = self.copyList()
        
        # add all the items in the second list in order
        current = b.head
        while current != None:
            newList.addInOrder(current.getData())
            current = current.getNext()
        
        # return the list
        return newList

    def isEqual (self, b):
        # Test if two lists are equal, item by item, and return True.
        equal = True
        
        # test if the lengths are the same
        if self.getLength() == b.getLength():
            currentA = self.head
            currentB = b.head
            # itterate through and see if any two items aren't the same
            while currentA != None:
                if currentA.getData() != currentB.getData():
                    equal = False
                currentA = currentA.getNext()
                currentB = currentB.getNext()
        else:
            equal = False
            
        # return True if the lists are equal, false otherwise
        return equal 

    def removeDuplicates (self):
        # Remove all duplicates from a list, returning a new list.
        #    Do not change the order of the remaining elements.
        newList = self.copyList()
        current = newList.head
        previous = None
        # this list holds all of the data that we've seen
        items = []
        
        # itterate through the nodes and remove any duplicates from the link
        while current != None:
            temp = current.getData()
            # if the item is a duplicate, remove it
            if temp in items:
                if previous == None:
                    newList.head = current.getNext()
                    previous = None
                    current = newList.head
                else:
                    previous.setNext(current.getNext())
                    current = previous.getNext()
            # if not, add the item to the list of items
            else:
                items.append(temp)
                previous = current
                current = current.getNext()
            
        # return the list with the duplicates removed
        return newList
    
    
def main():

    print ("\n\n***************************************************************")
    print ("Test of addFirst:  should see 'node34...node0'")
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
