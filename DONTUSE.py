def formatGame(a):
    setup = a
    # establish intitial output gamegameFrame reference values
    gameLine= "|"
    gameFrame = 1
    secRoll = False


    # run through each item of data and perform appropriate actions
    for i in range(len(setup)):

        if gameFrame == 10:
            if(setup[i] == "X" or setup[i+1]=="/"):
                gameLine += setup[i] + " " + setup[i+1] + " " + setup[i+2]                    
            else:
                gameLine += "  " + setup[i] + " " + setup[i+1]
            gameLine += "|"
            print(gameLine)
            break
        elif setup[i] == "X":
            gameLine += (str(setup[i]))
            gameLine += ("  |")
            gameFrame += 1
        elif secRoll == True:
            gameLine += " " + setup[i] + "|"
            secRoll = False
            gameFrame += 1
            continue

        

        # first ball of gameFrame
        else:
            gameLine += setup[i]
            secRoll = True

def findScore(a):
    # intialize variables
    frame = a
    secondRoll = False
    strike = False
    spare = False
    score = 0
    scoreLine = "|"
    gameFrame = 1
    

    for i in range(len(frame)):
        # last Frame

        if gameFrame == 10:
            
                    #if last game is a strike
                    if strike == True:
                        strike = False
                        for j in range(i, i+2):
                            #if strike again
                            if frame[j]=="X":
                                    score += 10
                            #if it is a miss
                            elif frame[j]=="/":
                                score += 10-int(frame[j-1])
                            elif frame[j]=="-":
                                score += 0
                            else:
                                score += int(frame[j])
                        scoreLine += str(score).rjust(3) + "|"

                    #if spare
                    if spare == True:
                        if frame[i] != "-":
                            #if strike after spare
                            if frame[i] == "X":
                                score += 10
                            else:
                                score += int(frame[i])
                        scoreLine += str(score).rjust(3) + "|"

                    #if strike
                    if frame[i]=="X":
                        if frame[i+2] == "/":
                            score += 20
                        elif frame[i+1] == "X":
                            if frame[i+2] == "X":
                                score += 30
                            elif frame[i+2] == "-":
                                score += 20
                            else:
                                score += 20 + int(frame[i+2])
                        else:
                            score += int(frame[i]) + int(frame[i+1])
                        scoreLine += str(score).rjust(5)
                        scoreLine += "|"
                        print(scoreLine)
                        break
                    #if it is a spare
                    if frame[i+1]=="/":
                        score += 10
                        if frame[i+2]=="X":
                            score += 10
                        elif frame[i+2]!="-":
                            score += int(frame[i+2])
                        scoreLine += str(score).rjust(5)
                        scoreLine += "|"
                        print(scoreLine)
                        break
                    # if it is a miss     
                    if frame[i+1]=="-":
                        if frame[i]!="-":
                            score += int(frame[i])
                    elif frame[i]=="-":
                        score += int(frame[i+1])
                    else:
                        score += int(frame[i+1]) + int(frame[i])           
                    
                    scoreLine += str(score).rjust(5)
                    scoreLine += "|"
                    print(scoreLine)
                    break

        # last frame is strike
        elif strike == True :
                    strike = False
                    for j in range(i, i+2):                
                        if frame[j]=="X":
                            score += 10
                        elif frame[j]=="/":
                            score += abs(int(frame[j-1])-10)
                        elif frame[j]=="-":
                            score += 0
                        else:
                            score += int(frame[j])
                    scoreLine += str(score).rjust(3) + "|"
    
        
        

        # second ball of gameFrame
        elif secondRoll == True:
                    secondRoll = False
                    
                    # check for spare
                    if frame[i] == "/":
                        if frame[i-1]=="-":
                            score += 10
                        else:
                            score += abs(int(frame[i-1])-10)
                        spare = True
                        gameFrame += 1
                        continue

                    # check for null
                    # if no null, add data to score
                    if frame[i] != "-" and frame[i] != "X":
                        score += int(frame[i])

                    scoreLine += str(score).rjust(3) + "|"
                    gameFrame += 1
                    continue
       
        if spare == True:
                    spare = False
                    if frame[i]=="X":
                        score += 10
                        strike = True
                    else:
                        score += int(frame[i])
                    scoreLine += str(score).rjust(3) + "|"
            
        
        #if strike make strike True
        if frame[i]=="X":
            score += 10
            strike = True
            gameFrame += 1
            continue
        #if miss, make secondRoll true
        if frame[i] == "-":
            secondRoll = True
            continue

        
        # first ball of gameFrame
        # no strike or null - add data to score and run iteration for second ball of gameFrame
        elif frame[i] != "-" and frame[i] != "/" and frame[i] != "X":
            score += int(frame[i])
            secondRoll = True


def main():
    
    # set up initial gamegameFrame output    
    

    # read in scores files    
    infile = open("scores.txt", "r")

    for line in infile:
        print("  1   2   3   4   5   6   7   8   9    10")
        print("+---+---+---+---+---+---+---+---+---+-----+")
        game = line
        game = game.strip()
        gameString = ""

        
        for i in range(len(game)):
            if game[i] != " ":
                gameString += game[i]

        
        formatGame(gameString)
        findScore(gameString)
        print("+---+---+---+---+---+---+---+---+---+-----+")
    infile.close()
main()
