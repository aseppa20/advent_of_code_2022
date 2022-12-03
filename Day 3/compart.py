from letters import lettersToNumbers as LTN

def cutInHalf(toBeHalved: str) -> tuple:
    halfPoint = len(toBeHalved)/2
    return (toBeHalved[:int(halfPoint)], toBeHalved[int(halfPoint):] )


def findDupes(stringPair: tuple):
    characters = []
    dupes = []

    for c1 in stringPair[0]:
        if c1 not in characters:
            characters.append(c1)
    
    for c2 in stringPair[1]:
        if c2 in characters and c2 not in dupes:
            dupes.append(c2)

    return dupes


def getLetterValue(char: str) -> int:
    return LTN[char]

###Part 2:
def findCommonInGroup(group: list) -> str:
    chars = []
    dupes = []
    triplets = []

    for c1 in group[0]:
        if c1 not in chars:
            chars.append(c1)

    for c2 in group[1]:
        if c2 in chars and c2 not in dupes:
            dupes.append(c2)

    for c3 in group[2]:
        if c3 in dupes and c3 not in triplets:
            triplets.append(c3)

    return triplets[0]

def main(inFile="input.txt"):
    result = 0
    result2 = 0

    with open(inFile, "r") as input:
        
        temp = []

        for line in input.readlines():
            lineInHalf = cutInHalf(line)
            for c in findDupes(lineInHalf):
                result += getLetterValue(c)
            if len(temp) == 2:
                temp.append(line)
                result2 += getLetterValue( findCommonInGroup(temp) )
                temp = list([])
            else:
                temp.append(line)
    
    print(result, result2)
    return (result, result2)


if __name__ == "__main__":
    main()
