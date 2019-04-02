#  File: ERsim.py
#  Description: Emergency Room simulation
#  Student's Name: Tyree Pearson
#  Student's UT EID: Tsp627
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 6-5-2017
#  Date Last Modified:6-5-2017

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
    
    def __str__(self):
        return str(self.items)

    

def main():

    file = open("ERsim.txt","r")
    criticalQ = Queue()
    seriousQ = Queue()
    fairQ = Queue()
    #Loop for all commands in file
    for line in file:
        strings = line.split()
        if "exit" in strings:#Exit command to break loop
        
            print("Command: Exit")
            break

        if "add" in strings: #Add command, adds patients to Queue

            if "Critical" in strings: #Most important queue, always goes first unless overiden
                criticalQ.enqueue(strings[-1])#get name from last element in list
                print("Command: Add patient",strings[-1]," to ",strings[1],"queue")
                print("   Queues are:")
                print("   Fair:",fairQ)
                print("   Serious:",seriousQ)
                print("   Critical:",criticalQ)
                print()
                continue

            elif "Serious" in strings: #Second important queue, unless overiden 
                seriousQ.enqueue(strings[-1])#get name from last element in list

            
                print("Command: Add patient",strings[-1]," to ",strings[1],"queue")
                print("   Queues are:")
                print("   Fair:",fairQ)
                print("   Serious:",seriousQ)
                print("   Critical:",criticalQ)
                print()
                continue
            elif "Fair" in strings: #Least important Queue
                fairQ.enqueue(strings[-1])#get name from last element in list

            
                print("Command: Add patient",strings[-1]," to ",strings[1],"queue")
                print("   Queues are:")
                print("   Fair:",fairQ)
                print("   Serious:",seriousQ)
                print("   Critical:",criticalQ)
                print()
                continue 
        elif "next" in strings:#Type of treat command that goes by order of importantance
            print("Command: Treat next patient")
            print()
            if not criticalQ.isEmpty() :    #Check for empty 

                print("   Treating Patient",criticalQ.peek())
                criticalQ.dequeue()         #remove from queue

            elif (not seriousQ.isEmpty() ):#Check for empty 
                print("   Treating",seriousQ.peek())
                seriousQ.dequeue()          #remove from queue


            elif  (not fairQ.isEmpty()) :   #check for empty 
                print("   Treating",fairQ.peek())
                fairQ.dequeue()             #remove from queue
            else:
                print("No patients in queues")
                                            #if no patients left any any queues
                continue
                
                
            print("   Queues are:")
            print("   Fair:",fairQ)
            print("   Serious:",seriousQ)
            print("   Critical:",criticalQ)
  

        elif ("all" in strings): #Treat all patients  
            print()
            print("Command: Treating all patients")
            #loop through until all queues are empty
            while (not criticalQ.isEmpty()) or  (not seriousQ.isEmpty()) or (not fairQ.isEmpty()):
                 #go through most important 
                if not criticalQ.isEmpty():

                    print("Treating",criticalQ.peek())
                    criticalQ.dequeue()
                #make sure critical is empty then go through serious
                elif ((criticalQ.isEmpty() is True) and (not seriousQ.isEmpty())):
                    print("Treating",seriousQ.peek())
                    seriousQ.dequeue()

                #make sure critical and serious are empty before going through fair
                elif ((seriousQ.isEmpty() is True) and (criticalQ.isEmpty() is True) and not fairQ.isEmpty()):
                    print("Treating",fairQ.peek())
                    fairQ.dequeue()
                else:
                    print("No patients in queues")
                    

                print("   Queues are:")
                print("   Fair:",fairQ)
                print("   Serious:",seriousQ)
                print("   Critical:",criticalQ)

        #Over ride commands the determine who gets treated next                
        else:
            if ("Fair" in strings):
                if not fairQ.isEmpty():
                    print("Treating",fairQ.peel())
                    fairQ.dequeue()
                else:
                    print("No patients in queues")
                    continue

            if "Critical" in strings:
                if not criticalQ.isEmpty():
                    print("Treating" ,criticalQ.peek())
                    criticalQ.dequeue()
                else:
                    print("No patients in queues")
                    continue
                    
                    

            elif ("Serious" in strings):
                if not seriousQ.isEmpty():
                    print("Treating",seriousQ.peek())
                    seriousQ.dequeue()
                else:
                    print("No patients in queues")
                    
            print("   Queues are:")
            print("   Fair:",fairQ)
            print("   Serious:",seriousQ)
            print("   Critical:",criticalQ)
            continue

    print()
    

    file.close()
main()

        
        
