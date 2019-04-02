#6/16/2017
#Assertion methods
#its a claim that x can be greater than 3
import random 

'''

def main():

    x1 = int(input("enter a number: "))
    x2 = int(input("entere a number: "))

    assert x2 != 0, "you cant divide by 0"

    print(x1/x2)

main()
             
'''


#GUESSSING GAME

#SUBCLASSES OF EXCEPTION CLASS
class SmallValueError(Exception):

    def __init__(self,guess):
        self.guess = guess

class LargeValueError(Exception):
    # WITE A INIT METHOD: 



def main():


    
    number = random.randint(1,100)
    print("I have selected a random int you have to guess it")

    while True:

        inputVal = int(input("Enter a guess: "))
        try:
            if inputVal < number:
                #BY RAISING THE ERROR IT DOESNT TERMINATE
                raise SmallValueError
            elif inputVal > number:
                #RAISES AND DOESNT TERMINATE PROGRAM 
                raise LargeValueError
            else:
                break
        #DOESNT TERMINATE THE PROGRAM 
        except SmallValueError as error :
            print("Your guess of ", error.guess," was to small.")
        except LargeValueError as mistake: 
            print("Your guess of ",mistake.guess,"was to small. ")

        print("you guessed it")

            
    
    
main()
