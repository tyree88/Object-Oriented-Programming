#  File: Friends.py
#  Description: Simple Facebook like application using LinkedLists
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 03/25/2017
#  Date Last Modified: 03/25/2017

#----------------------- Classes -----------------------#

class Node():
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
    
    
class UnorderedList():

    def __init__(self):
        self.head = Node(0) # sentinal, data is the length of the list

    def isEmpty (self):
        return self.head.getNext() == None

    def add (self, item):
        # add a new Node to the beginning of an existing list
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)
        # increment the length
        self.head.setData(self.head.getData() + 1)

    def length (self):
        return self.head.getData()

    def search (self, item):
        current = self.head.getNext()
        found = False

        while current != None and not found:
            if current.getData().name == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    # get the specific item, assuming the item is in the list
    def getItem(self, item):
        current = self.head.getNext()
        found = False

        while not found:
            if current.getData().name == item:
                found = True
            else:
                current = current.getNext()

        return current.getData()
        
    def remove (self, item):
        current = self.head.getNext()
        previous = self.head
        found = False

        while not found:
            if current.getData().name == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        previous.setNext(current.getNext())
        # decrement the length
        self.head.setData(self.head.getData() - 1)
        
    def __str__ (self):
        # Return a string representation of data suitable for printing.
        current = self.head.getNext()
        data = []
        
        # itterate through the list and pull out all of the data
        while current != None:
            data.append(current.getData())
            current = current.getNext()
            
        # format the string
        st = "[ "
        for d in data:
            st += str(d)
            st += " "
        st += "]"

        # print all of the nodes two spaces apart, ten to a line
        return st

class User:
    
    def __init__(self, name):
        self.name = name
        self.friends = UnorderedList()
        
    def __str__(self):
        return self.name
    
#----------------------- Functions -----------------------#

def runCommand(users, lineDict):
    '''
    Runs the command given by checking for errors, printing messages, and updated all of the lists
    '''
    command = lineDict["command"]
    people = lineDict["people"]
    
    # check if each of the users exist
    if(command != "Person"):
        # itterate through the people and check if they exist or not
        # keep count in people didn't exist
        notPCount = 0
        for p in set(people):
            print(people)
            if(not users.search(p)):
                print("A person with name %s does not currently exist." % (p))
                notPCount += 1
                
        # if someone didn't exist, exit
        if (notPCount > 0):
            print()
            return
    
    # Person Command
    if (command == "Person"):
        # if the user is a duplicate, print the appropriate message 
        if(users.search(people[0])):
            print("A person with name %s already exists." % (people[0]))
        else:
            print("%s now has an account." % (people[0]))
            # create and add the user
            user = User(people[0])
            users.add(user)
    
    # Friend Command        
    elif (command == "Friend"):
        # a person can't friend theirself
        if(people[0] == people[1]):
            print("A person cannot friend him/herself.")
        # check if they are already friends or not
        elif( users.getItem(people[0]).friends.search(people[1]) ):
            print("%s and %s are already friends." % (people[0], people[1]))
        else:
            print("%s and %s are now friends." % (people[0], people[1]))
            # get the users
            p1 = users.getItem(people[0])
            p2 = users.getItem(people[1])
            # add the friends to each other
            p1.friends.add(p2)
            p2.friends.add(p1)
    
    # Unfriend Command        
    elif (command == "Unfriend"):
        # a person can't unfriend theirself
        if(people[0] == people[1]):
            print("A person cannot unfriend him/herself.")
        elif( not users.getItem(people[0]).friends.search(people[1]) ):
            print("%s and %s aren't friends, so you can't unfriend them." % (people[0], people[1]))
        else:
            print("%s and %s are no longer friends." % (people[0], people[1]))
            # get the users
            p1 = users.getItem(people[0])
            p2 = users.getItem(people[1])
            # remove the friends from each other
            p1.friends.remove(p2.name)
            p2.friends.remove(p1.name)
      
    # print all of the person's friends
    elif (command == "List"):
        p = users.getItem(people[0]).friends
        if(p.isEmpty()):
            print("%s has no friends." % (people[0]))
        else:
            print(p)
    
    # print whether or not the two people are friends
    elif(command == "Query"):
        p1 = users.getItem(people[0])
        p2 = users.getItem(people[1])
        if(p1.friends.search(p2.name)):
            print("%s and %s are friends." % (people[0], people[1]))
        else:
            print("%s and %s are not friends." % (people[0], people[1]))
        
            
    print()
    return

#----------------------- Main -----------------------#

def main():
    pass
    # Create a LinkedList for all the users
    users = UnorderedList()

    # Read in the text file of commands
    infile = open("FriendData.txt", "r")
    print()
    
    # Itterate through all of the commands
    for line in infile:
        line = line.split()
        lineDict = {"command": line[0], "people": line[1:]}
        print(lineDict)
        # if exit, return True
        if(lineDict["command"] == "Exit"):
            print("Exiting...")
            print()
            break
        else:
            runCommand(users, lineDict)
    print(lineDict)
    
    # close the file
    infile.close()
    
    
if __name__ == "__main__":
    main()
