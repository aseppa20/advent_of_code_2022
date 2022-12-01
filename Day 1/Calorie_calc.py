def readData(fileName):
    ### Read a file and return an array of summed values
    f = open(fileName, "r")
    
    returnable = []
    sumOfRound = 0

    for line in f.readlines():
        line.strip()
        if line != "\n":
            sumOfRound += int(line)
        else:
            returnable.append(sumOfRound)
            sumOfRound = 0

    returnable.append(sumOfRound)
    
    return returnable

def findMax(list):
    ### Finds the max value
    return max(list)

def findMaxTopThree(list):
    returnable = []

    for i in range(3):
        returnable.append( findMax(list) )

        for y, val in enumerate(list):
            if returnable[i] == val:
                list.pop(y)
                break
    
    return returnable

def main():
    elves = readData( "input.txt" )
    print( findMax(elves) )
    print( sum( findMaxTopThree(elves) ) )

if __name__ == "__main__":
    main()