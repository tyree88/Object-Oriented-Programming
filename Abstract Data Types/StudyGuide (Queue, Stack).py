#STUDY GUIDE 2
import random
class Stack (object):
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
    
##############################################################################
# QUEUE QUEUE   QUEUE   QUEUE   QUEUE   QUEUE   QUEUE   QUEUE QUEUE
#############################################################################
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

    
##############################################################################

# Get ready, do tasks function

##############################################################################
def getReady(tasks):

    actions = tasks.split()
    day = Queue()
    for i in actions:
        
        day.enqueue([i])
    while (day.size()) > 0:
        print("I will now do ", day.dequeue())
    return("Now its time for work!")

    
##############################################################################

#Hot potatoe 

##############################################################################   
def hotPotato(nameList,num):
    
    q = Queue()
    names = nameList.split()
    random.shuffle(names,random.random)
    
    
    print(names)
    
    for i in names:
        q.enqueue(i)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        print("THIS MAN DID NOT MAKE IT:", q.peek())
        q.dequeue()
    return ("Winner is:",q.dequeue())

    
##############################################################################

# Post Fix conversion from infix

##############################################################################
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#############################################################################

# POST FIX PROBLEM 

#############################################################################

def postfix(values):
    operandStack = Stack()
    tokenList = values.split()
    #check the values in tokenList
    for token in tokenList:
        if token in "/*+-":
            op1 = operandStack.pop()
            op2 = operandStack.pop()
            #FIND RESULT
            if token =="*":
                result = op1 *op2
            elif token == "/":
                result = op1/op2
            elif token == "+":
                result = op1+op2
            else:
                result = op1 - op2
            operandStack.push(result)
            print("found operator '"+token+"': popping",op2,"and",op1)
            print("pushing",op2,token,op1,"   stack now: ",operandStack)
        else:
            operandStack.push(int(token))
            print("pushing",token,"   stack now: ",operandStack)
    return operandStack.pop()
            
#############################################################################

# symbol Checker 

############################################################################
def symbolchecker(symbolString):

   s = Stack()
   balanced = True
   index = 0
   print("Testing string ",symbolString)

   while index < len(symbolString) and balanced:

      symbol = symbolString[index]

      print("symbol:",symbol)
      if symbol in "([{<":
         s.push (symbol)
         print("   pushed: stack now ",str(s))
         input("paused")
      else:
         # there had better be a matching open paren on the stack
         if s.isEmpty():
            balanced = False
            print("   Stack is empty! Aborting")
            input("paused")
         else:
            top = s.pop()
            if not matches (top,symbol):
               balanced = False
               print("   Mismatch found! Aborting")
               input("paused")
            else:
               print("   Match found: stack after pop now: ",str(s))
               input("paused")

      index += 1

   # while loop is over
   if balanced and s.isEmpty():
      return True
   else:
      return False




def matches (opened, close):
    opens = "({[<"
    closes = ")}]>"

    return opens.index(opened) == closes.index(close)
    
                
            

def main():


    #POST FIX CONVERSION SAMPLE 
    #print(infixToPostfix("A * B + C * D"))
    #print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

    #postFix problem examples
    problem = "3 3 * 60 +"
    anwser = postfix(problem)
    print(anwser)


    #SAYING ORDER OF TASK PROBLEM
    tasks = "Coffee Drink Shower Teeth Dress Leave"
    print(getReady(tasks))

    nameList = "Tyree Kanye Childish Boi Watermalone"
    
    print(hotPotato(nameList, 7))

    
    #SYMBOL CHECKER EXAMPLES
    #example = "{[]}<>"
    #example2 = "{]()"
    #print(symbolchecker(example2))


    
main()
