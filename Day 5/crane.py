STACKS = [[],[],[],[],[],[],[],[],[],[]]

def buildStacks(filename: str):
    with open(filename, "r") as file:
        lineReader = 1
        pos = 1

        for line in file.readlines():

            if line[lineReader] == "1":
                break

            while lineReader < len(line):
                if line[lineReader] != " ":
                    STACKS[pos].insert(0, line[lineReader])
                lineReader += 4
                pos += 1
            
            lineReader = 1
            pos = 1
        
        file.close()


def parseInstructions(instruction: str) -> tuple:
    instruction = instruction.split(" ")
    return (int(instruction[1]), int(instruction[3]), int(instruction[5])) # move 1 from 2 to 1


def executeInstructions(instruction: tuple):
    for i in range(instruction[0]):
        STACKS[instruction[2]].append( STACKS[instruction[1]].pop() )


def executeInstructionsP2(instruction: tuple):
    for i in range(instruction[0]):
        STACKS[0].append( STACKS[instruction[1]].pop() )
    
    for i in range(instruction[0]):
        STACKS[instruction[2]].append( STACKS[0].pop() )


def readTops() -> str:
    result = ""
    for node in STACKS:
        try:
            result += node[-1]
        except IndexError:
            continue
    
    return result


def main(filename="input.txt", ver=2):
    
    buildStacks(filename)

    if ver == 1:
        with open(filename, "r") as file:
            for line in file.readlines():
                
                if line.find("move") < 0:
                    continue

                executeInstructions( parseInstructions(line) )

            file.close()
    
    else:
        with open(filename, "r") as file:
            for line in file.readlines():
                
                if line.find("move") < 0:
                    continue

                executeInstructionsP2( parseInstructions(line) )

            file.close()    


    print( readTops() )


if __name__ == "__main__":
    main()
