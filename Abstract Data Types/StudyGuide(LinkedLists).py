import random 
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
class LinkedList ():

    def __init__(self):
      self.head = None

    def isEmpty (self):
      return self.head == None

    def add (self,item):
      # add a new Node to the beginning of an existing list
      temp = Node(item)
      temp.setNext(self.head)
      self.head = temp
    def length (self):
      current = self.head
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

    def search (self,item):
      current = self.head
      found = False

      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

    def remove (self,item):
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext())

    def findOrdered (self, item):
        current = self.head
        found = False
        stop = False
        while current!= None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
    def remove(self,item):
        #create a search function
        previous = None
        found = False
        current = self.head
        while current!= None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = currnet.getNext()
        else:
            previous.setNext(current.getNext())
    def iListSum(self):
        current = self.head
        total = 0
        while current != None:
            total+= current.getData()
            current = current.getNext()
        return total
    def rListSum(self,node):
        current = self.head
        prev = None
        if current == None and prev == None :
            return 0
        else:
            prev = current
            current = current.getNext()
            return prev.getData() + current.getData() +self.rListSum(current)


    def __str__(self):
        current = self.head
        nodes = []
        elements = ''
        while current != None:
            nodes.append(current.getData())
            current = current.getNext()
        for i in range(len(nodes)):
            elements += str(nodes[i]) + " "
        return elements

##############################################################################

#Circular linked list 

##############################################################################
class QueueLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, item):
    #Adds value to end of queue
        temp = Node(item)
        if self.head == None:
            self.head = self.tail = temp #there has to be a new linked node represented
        #if there is a tail. that its not empty 
        else:
            
            self.tail.next = temp # creates a new pointer 
            self.tail = temp # creates a new node

    def isEmpty(self):
        return self.head == None

    def remove(self,item):
        current = self.head.getData() #gets the current value 
        self.head = self.head.getNext()
        
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                
        #Checks first value in the Queue 
        if self.head == None:
            self.tail = None

    def __str__(self):
        current = self.head
        nodes = []
        elements = ''
        while current != None:
            nodes.append(current.getData())
            current = current.getNext()
        for i in range(len(nodes)):
            elements += "[  "

            elements += str(nodes[i])+ "  " + "]"
           
        return elements

def main():
    myLink = LinkedList()
    for i in range(10):
        myLink.add(i)
    print(myLink)
    print("My lists sum is :",myLink.iListSum())
    current = myLink.head
    print("My recursive list sum is : ",myLink.rListSum(current))
    
    mylist = QueueLinkedList()
    for i in range(10):
        
        mylist.add(random.randint(1,25))
    print(mylist)
    
    
                   
main()
        
    
