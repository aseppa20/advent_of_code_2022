TOTAL_SIZE_COUNT = 0

def addToCount(num):
    if num and num <= 100000:
        global TOTAL_SIZE_COUNT
        TOTAL_SIZE_COUNT += num

def parseLine(line: str):
    line = line.strip()
    line = line.split(" ")

    if line[0] == "dir":
        return None

    if line[0] == "$":
        if line[1] == "ls":
            return None
        if line[1] == "cd":
            return line[2] #.. = Out stack #other to stack
    
    return line[0]

def main(filename: str="input.txt"):
    
    global TOTAL_SIZE_COUNT
    TOTAL_SIZE_COUNT = 0

    stack = []
    max_space = 70000000
    needed_space = 30000000
    used_space = 0

    with open(filename, "r") as file:
        
        for line in file.readlines():
            line = parseLine(line)
            
            if line == None:
                continue
            
            if line == "..":
                closingSize = stack.pop()
                addToCount(closingSize)
                stack[-1] += int(closingSize)
                continue

            if line.isdigit():
                stack[-1] += int(line)
                continue

            stack.append(0)
        
        used_space = sum(stack)
        file.close()

    to_be_removed = max_space
    goal = abs(max_space - used_space - needed_space)

    with open(filename, "r") as file:
        
        for line in file.readlines():
            line = parseLine(line)
            
            if line == None:
                continue
            
            if line == "..":
                closingSize = stack.pop()
                
                if closingSize < to_be_removed and goal < closingSize:
                    to_be_removed = int(closingSize)

                stack[-1] += int(closingSize)
                continue

            if line.isdigit():
                stack[-1] += int(line)
                continue

            stack.append(0)
        
        while len(stack) != 1:
            closingSize = stack.pop()
                
            if closingSize < to_be_removed and goal < closingSize:
                to_be_removed = int(closingSize)

            stack[-1] += int(closingSize)
        
        file.close()

    return(TOTAL_SIZE_COUNT, to_be_removed)
      
            
if __name__ == "__main__":
    print(main())