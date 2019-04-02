#  File: Bowling.py
#  Description:
#  Student's Name: Tyree Pearson
#  Student's UT EID: tsp627
#  Course Name: CS 313E 
#  Unique Number: XXXXX
#
#  Date Created:
#  Date Last Modified:
def roll_frame(setup):
    gameLine = "|"
    gameFrame = 1
    secRoll = False
    #format for each frame
    for i in range(len(setup)):
        #strike formating for last Frame
        if gameFrame == 10:
            if(setup[i] =="X" or setup[i+1] =="/"):
                gameLine += setup[i] + " " + setup[i+1] + " " + setup[1+2]
            else:
                gameLine += " " +setup[i] + "" +setup[i+1]
            gameLine += "|"
            print(gameLine)
            break
        elif secRoll == True:
            gameLine += "  " + setup[i] + "|"
            secRoll = False
            gameFrame +=1
            continue
        elif setup[i] == "X":
            gameLine += str(setup[i])
            gameLine += ("   |")
            gameFrame += 1
        
        else:
            gameLine += setup[i]
            secRoll = True
            
        
            
            
        

def find_score(a):
        frame = a
        print(frame)
        strike = False
        spare = False
        secondRoll = False
        score = 0
        scoreLine = "|"
        scoreFrame = 1                
                
                
        
        
        for i in range(len(frame)):
                #Only For the 10th FRAME
                if scoreFrame == 10:

                            if strike == True:
                                strike = False
                                for j in range(i, i+2):
                                    
                                    if frame[j] == "X":
                                        score += 10
                                    elif frame[j]== "-":
                                        score = score + 0
                                    elif frame[j] == "/":
                                        score += int(frame[j-1]) + 10
                                    else:
                                        score = score + int(frame[j])
                                scoreLine += str(score).rjust(3) + "|"

                            elif spare == True:
                                if (frame[i] != "-"):
                                    if (frame[i] == "X"):
                                        score += 10
                                    else:
                                        score += int(frame[i])
                                scoreLine += str(score).rjust(3)+"|"
                            #if last roll is strike
                            elif(frame[i]=="X"):
                                if frame[i+2] == "/":
                                     score += 20
                                elif frame[i+1] == "X":
                                    if frame[i+2] == "X":
                                        score += 30
                                    #if roll after is a miss
                                    elif frame[i+2] != "-":
                                        score += 20 
                                    #if it is a hit
                                    else:
                                        score += 20 + int(frame[i+2])
                                  #if it is a 
                                else:
                                    score += int(frame[i]) + int(frame[i+1])
                                scoreLine += str(score).rjust(5)
                                scoreLine += "|"
                                print(scoreLine)
                            
                                break
                            #if Spare
                            if frame[i+1] == "/":
                                score += 10
                                if frame[i+2] == "X":
                                    score = score + 10
                                elif frame[i+2] != "-":
                                    score += int(frame[i+2])
                                scoreLine += str(score).rjust(5)
                                scoreLine+= "|"
                                print (scoreLine)
                                break

                            if(frame[i+1]=="-"):
                                if(frame[i]!="-"):
                                    score += int(frame[i])
                            elif(frame[i]=="-"):
                                score += int(frame[i+1])
                            else:
                                score += int(frame[i+1]) + int(frame[i])

                            scoreLine += str(score).rjust(5)
                            scoreLine += "|"
                            print(scoreLine)
                            break
                            #FINALLY DONE WITH LAST FRAME

                

                
                #if it is a STRIKE
                elif strike == True:
                            strike = False
                            for j in range(i,i+3):
                             
                                if frame[i] == "X":
                                    score += 10
                                elif frame[j]=="/":
                                    score = abs(int(frame[j-1])-10)
                                elif frame[j]=="-":
                                    score += 0
                                else:
                                    score += int(frame[j])
                            scoreLine += str(score).rjust(3)+"|"

                            
                #if it is the SECOND ROLLL
                elif secondRoll== True:
                            secondRoll = False
                            if frame[i] == "/":
                                if frame[i-1] == "-":
                                    score +=10
                                else:
                                    score += abs(int(frame[i-1])-10)
                                spare = True
                                scoreFrame +=1
                                continue
                            
                            elif frame[i] != "-" and frame[i] != "X":
                                score += int(frame[i])
                            scoreLine += str(score).rjust(3) + "|"
                            scoreFrame +=1
                            continue
                        

                
                # if it is a SPARE
                elif spare:
                    spare = False
                    if frame[i] =="X":
                       score += 10
                       strike = True
                       
                    else:
                        score += int(frame[i])
                    scoreLine += str(score).rjust(3)+"|"
                    
                

                    
                #Make Strike True
                elif frame[i] == "X" :
                    score +=10
                    strike = True
                    scoreFrame +=1
                    continue
                #create a second roll
                elif frame[i] == "-":
                    secondRoll = True
                    continue
            

                elif frame[i] != "-" and frame[i] != "/" and frame[i] != "X":
                    score += int(frame[i])
                    secondRoll = True
                    


def main():
    #open and read file 
    infile = open("scores.txt", "r")

    print("  1   2   3   4   5   6   7   8   9   10")
    print("+___+___+___+___+___+___+___+___+___+_____+")   
    
    for line in infile:
        send = ""
        lst = line.strip()
        for i in range(len(lst)):
            if lst[i] != " ":
                send += lst[i]
                
           
        roll_frame(send)
        find_score(send)

        
    

    
        print("+---+---+---+---+---+---+---+---+---+-----+")
    infile.close()
main()

    
    
