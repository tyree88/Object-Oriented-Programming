#6/14/17
#Quarter Back Rating
'''
def main():

    touchdowns = 85
    interceptions = 0

    #like an if statment, but checks through the whole block of statments for the Exception Error
    try:
        TIratio = touchdowns / interceptions
        print(TIratio)
    except: ZeroDivisionError:
        TIratio = "undetermined"
        print("QB hasnt thrown an interception")
    if TIratio = "undetermined":
        print("The QB ratio cannot be determined")
    
    
'''

'''

# sumDigits(s) that takes a string and finds the sum of the decimal
def sumDigits(s):

    sum = 0
    for char in s:
         try:           
            sum += int(char)
        except: ValueError:
            print("skipped", char)

            
    return sum


'''
def findEven(alisT):
    try:
        for cal in alist:
            if val%2 == 0:
                return(val)
        #if made it through the ntire ist with out finding an even number
        #doing a Raise you can define your own Error message
        raise ValueError("only odd numbr")
    
    except ValueError:
        print("only odd numbers in the list")
        return(-1)


def main():
    
        #print(sumDigits("1234"))
    
        '''
        while :
            val = input("Enter an interger: ")

            try:
                val = int(val)
                print("square of the number you entered is: ", val*val)
                break
                
            except ValueError:
                print(val, "is not an integer")
        '''

        #Creating an expection, Function FindEven(alist) that return the dirst even number if alest)

        
        
            
        
    

    


main():
