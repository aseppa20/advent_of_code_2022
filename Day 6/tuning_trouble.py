def findSequenceStart(datastream: str) -> int:
    readHead = 2
    while len(datastream) > readHead:
        
        readHead += 1

        if datastream[readHead] == datastream[readHead-1]:
            continue
        
        if datastream[readHead] == datastream[readHead-2]:
            continue

        if datastream[readHead] == datastream[readHead-3]:
            continue

        if datastream[readHead-1] == datastream[readHead-2]:
            continue

        if datastream[readHead-1] == datastream[readHead-3]:
            continue

        if datastream[readHead-2] == datastream[readHead-3]:
            continue

        return readHead + 1


def findMessageStart(datastream: str, sliceSize: int = 14):
    readHead = int(sliceSize)
    while len(datastream) > readHead:
        slice = datastream[int(readHead) - int(sliceSize) : int(readHead)]
        
        for ci, char in enumerate(slice):
            if slice.find(char) > -1 and ci != slice.find(char):
                break
        else:
            return readHead
        
        readHead += 1


def main(filename="input.txt"):
    with open(filename, "r") as file:
        line = file.readline()
        
        print(findSequenceStart( line ))
        print(findMessageStart( line , 4))
        print(findMessageStart( line ))
        
        file.close()

if __name__ == "__main__":
    main()
