class Stack:
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items[-1]

   def size (self):

      return len(self.items)
   def __str__(self):
      return str(self.items)

##################################################
def filterTag(tags):
   exceptions = ["meta", "br", "hr"]
   validTags = []
   
   t = Stack()
   #Go through each tag 
   for tag in tags:

      #check for exception tag
      if tag in exceptions:
         print("Tag",tag,"does not need to match: stack is", str(t))
         
         continue #continue on to next loop because no matching tag
      

      if tag not in validTags:

         #start of a tag
         if tag[0] != '/':
            #check if tag is not in valid tags
               validTags.append(tag) # add to list of valid tags
               print("New tag", tag,"found and added to list of valid tags")
               
               
               t.push(tag) #push to top of stack
               print("Tag %s pushed:  stack is now %s" % (tag, t))            
         else:
            validTags.append(tag)
            #Matching tag found
            lastTag = t.pop()

            if ("/"+lastTag) == tag:
               
               print("Tag", tag," matches top of stack: stack is now",str(t))
               continue

            if t.isEmpty():
               print("Stack is empty, all matches found")
               return
            else:
               #If an exception is found"
               return
   print()
            
   #If stack is empty then all tags have been filtered and found
   if t.isEmpty():
      print("Process complete all matches found")
      
   
   
   validTags.sort()

   print("VALID TAGS = ", validTags)
   print("EXCEPTIONS = ", exceptions)
   


def getTag(file):
    openB = "<"
    closeB = ">"
    tags = []
    for i in range(len(file)):
        
        #if string contains the start of a bracket
        if file[i] == "<":
            tag = ''
            i+=1
           #Gather everything in between the brackets
            while (file[i] != closeB and file[i] != " ") and i<= len(file):
                tag+= file[i]#create string for whats in between the brackets
                i+=1 #iterates through the len of each line in the file

            tags.append(tag) #put every tag into a list

    return tags

def main():

    infile = open("HTML.txt", "r")

    html = infile.readlines()
    allTags = []
    for line in html:

        allTags += getTag(line)

    print(allTags)
    filterTag(allTags)
    infile.close()

main()
