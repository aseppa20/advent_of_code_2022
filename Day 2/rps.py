#A (Rock 1) Y (Paper (Tie))
#B (Paper 2) X (Rock (Win))
#C (Scissors 3) Z (Scissors (Lose))


#SCORE_OPPONENT = 0

import time

def translateStrategy(rpsPair):
    
    #Player Opponent:
    if rpsPair[0] == 'A':
        rpsPair[0] = 1

    elif rpsPair[0] == 'B':
        rpsPair[0] = 2
    
    else:
        rpsPair[0] = 3
    
    #Player Me:
    if rpsPair[1] == 'Y':
        rpsPair[1] = 2

    elif rpsPair[1] == 'X':
        rpsPair[1] = 1
    
    else:
        rpsPair[1] = 3
    
    return rpsPair

def translateStrategyBetter(rpsPair):
    #Player Opponent:
    if rpsPair[0] == 'A': #Rock
        rpsPair[0] = 1

    elif rpsPair[0] == 'B': #Paper
        rpsPair[0] = 2

    else: #Sci
        rpsPair[0] = 3

    #Player Me:
    if rpsPair[1] == 'Y': #Tie
        rpsPair[1] = rpsPair[0]

    elif rpsPair[1] == 'Z': #Win

        if rpsPair[0] == 1: #Rock
            rpsPair[1] = 2 #Paper
        elif rpsPair[0] == 2: #Paper
            rpsPair[1] = 3 #Sci
        else: #Sci
            rpsPair[1] = 1 #Rock
    
    else: #Lose
        if rpsPair[0] == 1: #Rock
            rpsPair[1] = 3 #Sci
        elif rpsPair[0] == 2: #Paper
            rpsPair[1] = 1 #Rock
        else: #Sci
            rpsPair[1] = 2 #Paper
    
    return rpsPair

def rps( rpsPair ):

    if int(rpsPair[0]) == int(rpsPair[1]):
        return rpsPair[1] + 3
    
    #Player loses:
    if int(rpsPair[0]) == 1 and int(rpsPair[1]) == 3 or int(rpsPair[0]) == 2 and int(rpsPair[1]) == 1 or int(rpsPair[0]) == 3 and int(rpsPair[1]) == 2:
        return rpsPair[1]
    
    return rpsPair[1] + 6
    

def main():
    scorePlayer = 0
    scorePlayerBetter = 0

    f = open("input.txt", 'r')
    for line in f.readlines():
        line = line.rstrip()
        players = line.split(" ")
        players2 = list(players)
        scorePlayer += rps( translateStrategy( players ) )
        scorePlayerBetter += rps( translateStrategyBetter( players2 ) )

    print(f"Part 1: {scorePlayer}")
    print(f"Part 2: {scorePlayerBetter}")

if __name__ == "__main__":
    main()
