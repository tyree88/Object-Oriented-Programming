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

class UnorderedList ():
   #Sentinal List
   def __init__(self):
      sentinel = Node(None)
      self.head = sentinel

   def isEmpty (self):
      return self.head.getNext() == None

   def add (self,item):
      # add a new Node to the beginning of an existing list
      temp = Node(item)
      temp.setNext(self.head.getNext())
      self.head.setNext(temp)

   def length (self):
      current = self.head.getNext()
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def search (self,item):
      current = self.head.getNext()
      found = False

      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

   def remove (self,item):
      current = self.head.getNext()
      previous = self.head
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      previous.setNext(current.getNext())

   def helpGetData(self, item):
       current = self.head.getNext()
       found = False
       while not found:
           if current == None:
               return 
           if current.getData().name == item:
               found = True
           else:
               current = current.getNext()
       return current.getData()

   def __str__(self):
        current = self.head.getNext()
        links = []
        element = "[  "
        while current!= None:
            links.append(current.getData())
            current = current.getNext()
            
        for i in links:
            element +=str(i)
            element += "  "
        element += "]"
        return element
        
 

class User:

    def __init__ (self,name):
        self.name = name
        self.friend = UnorderedList()
    def __str__(self):
        return self.name

def runCommand(users,lineValue):
    commands = lineValue["command"]
    persons = lineValue["persons"]
    exist = False
    if commands != "Person":
        for i in persons:
            if users.helpGetData(i) == None:
                print()
                fake = i
                exist = True


            
                
    #PERSON
    if commands == "Person":
        print("-->  Person",persons[0])
        #if there is a user in the system already
        if (users.search(persons[0])):
            print("    This person with name",persons[0],"already exists.")
        else:
            print("    ",persons[0],"now has an account")
            #create new user
            new = User(persons[0])
            users.add(new) #Add to UL
        

 
    #FRIEND
    if commands =="Friend":

        print("-->  Friend",persons[0],persons[1])
        if exist:
                print("     A person with name",fake,"does not currently exist")
                print()
                return

        #if you friend yourself
        if persons[0] == persons[1]:
            print("     A person cannot friend themselves")
        #if already friends
        elif(users.helpGetData(persons[0]).friend.search(persons[1])):
             print("    ",persons[0],"and",persons[1],"are already friends")
        #not friends yet
        else:
             print("    ",persons[0],"and",persons[1],"are now friends")
             
             #Gather each user and create a link that
             #connects them to each others friend list
             friend1 = users.helpGetData(persons[0])
             friend2 = users.helpGetData(persons[1])
             #connect both friends to each others list 
             friend1.friend.add(persons[1])
             friend2.friend.add(persons[0])
    #UNFRIEND
    elif commands =="Unfriend":
        print("-->  Unfriend",persons[0],persons[1])
        if exist:
                print("     A person with name",fake,"does not currently exist")
                print()
                return
        #if you friend yourself
        if persons[0] == persons[1]:
            print("     A person cannot unfriend themselves")
        #if not friends
        elif(not users.helpGetData(persons[0]).friend.search(persons[1]) )or (not users.helpGetData(persons[1]).friend.search(persons[0])):
             print("     A person cannot unfriend someone that is not a friend")
        #unfriend friend
        else:
            print("    ",persons[0],"is unfriending", persons[1])
            #Gather each user and remove a link between them
            friend1 = users.helpGetData(persons[0])
            friend2 = users.helpGetData(persons[1])
            #remove the link
            friend1.friend.remove(friend2.name)#removes the name from the link by name
            friend2.friend.remove(friend1.name)#removes the name from the link by name
    #LIST
    elif commands == "List":
        print("-->  List",persons[0])
        if exist:
                print("     A person with name",fake,"does not currently exist")
                print()
                return
        #search the specific user then find and get all his friend
        #if they have no friends :(
        people = users.helpGetData(persons[0]).friend
        if people.isEmpty():
            print("    ",persons[0],"has no friends")
        else:
            space = "    "
            print(space,people)
    #QUERY
    elif commands == "Query":
        print( "-->  Query", persons[0],persons[1])

        if exist:
                print("     A person with name",fake,"does not currently exist")
                print()
                return
        #Check if two people are friends
        friend1 = users.helpGetData(persons[0])
        friend2 = users.helpGetData(persons[1])
        #search through friends1 linked friends list for other friend
        if friend1.friend.search(friend2.name):
            print("    ",persons[0],"and",persons[1],"are friends")
        else:
            print("    ",persons[0],"and",persons[1],"are not friends")

    print()
    return
        
        


def main():

    infile = open("FriendData.txt","r")
    users = UnorderedList()
    commands = []
    friends = []
    
    for line in infile:
        line = line.split()

        lineValue = {"command": line[0], "persons": line[1:]}
        # if exit, return True
        if(lineValue["command"] == "Exit"):
            print("-->  Exit")
            print("     Exiting...")
            print()
            break
        else:
            runCommand(users, lineValue)

        
    infile.close()
        
        
main()
        
