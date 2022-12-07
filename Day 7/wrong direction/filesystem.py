### THIS FILE DOES NOT SOLVE THE PROBLEM
### I wanted to include this file, since it shows how I wrongfully aproached the problem
### I also learned a lot while doing this file, so win-win I guess?

import sys
sys.setrecursionlimit( 10000 )

class Dir:
    name = ""
    files = [] #Files are tuples with (size , filename)
    dir = []
    total_size = 0

    def __init__(self, name: str):
        self.name = name

    def getName(self):
        return self.name
    
    def getFiles(self):
        return self.files
    
    def getDir(self):
        return self.dir

    def getSize(self):
        return self.total_size
    
    def addFile(self, file: tuple):
        self.files.append(file)
        self.total_size += file[0]

    def addDir(self, dir):
        self.dir.append(dir)
    
    def addToSize(self, dirSize):
        if dirSize:
            self.total_size += dirSize


class readFile:
    _file = None
    latestLine = ""
    def __init__(self, name: str = "input.txt"):
        self._file = open(name, "r")
    
    def getLatestLine(self) -> str:
        return self.latestLine
    
    def nextLine(self) -> str:
        self.latestLine = self._file.readline()
        return self.latestLine
    

    def close(self):
        self._file.close()



COMMANDS = None
TOTAL_SIZE_COUNT = 0
I = 0

def addToCount(num):
    if num and num <= 100000:
        global TOTAL_SIZE_COUNT
        TOTAL_SIZE_COUNT += num


def newDir(directory: Dir, name: str):
    directory.addDir( Dir(name) )
    return directory


def addNewFile(directory: Dir, file: tuple):
    directory.addFile(file)
    return directory


def parseLine(line: str) -> tuple:
    line = line.strip()
    line = line.split(" ")

    if line[0] == "$":
        if line[1] == "ls":
            return None
        if line[1] == "cd":
            return ('cd', line[2])
    
    if line[0] == "dir":
        return ('d', line[1])
    
    try:
        return ("nf", (int(line[0]), line[1]))
    except ValueError:
        return ('cd', '..')


def partOneCount(directory: Dir):
    
    if directory.getDir() != []:
        for d in directory.getDir():
            partOneCount(d)
    
    addToCount(directory.getSize)


def exploreDirectories(directory: Dir):
### Recursive: What directory we are currently in
    def _findDirID(name):
        for i, dname in enumerate(directory.getDir()):
            if dname.getName() == name:
                return i

    global I

    while COMMANDS.nextLine() != "" or directory.getName() != "/":
        cmd = COMMANDS.getLatestLine()
        cmd = parseLine(cmd)

        if cmd == None:
            continue

        elif cmd[0] == 'd':
            newDir(directory, cmd[1])
        
        elif cmd[0] == 'nf':
            addNewFile(directory, cmd[1])
        
        elif cmd[0] == 'cd' and cmd[1] == '..':
            return directory.getSize()
        
        elif cmd[0] == 'cd':
            num = _findDirID(cmd[1])
            folderSize = exploreDirectories( directory.getDir()[num] )
            directory.addToSize(folderSize)
    
    directory.addToSize(directory.getSize())
    partOneCount(directory)
    return directory.getSize()


def main(filename: str="input.txt"):
    global COMMANDS
    global TOTAL_SIZE_COUNT
    COMMANDS = readFile(filename)
    
    bootUp = COMMANDS.nextLine()
    bootUp = parseLine(bootUp)

    root = exploreDirectories( Dir( bootUp[1] ) )
    print(root)
    print(TOTAL_SIZE_COUNT)

    return TOTAL_SIZE_COUNT


if __name__ == "__main__":
    main()
