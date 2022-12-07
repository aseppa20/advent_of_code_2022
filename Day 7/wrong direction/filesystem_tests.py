import pytest
import filesystem as fs

#Dir tests:
#def Dir_tests():
#    root = fs.Dir("/")
#    assert root.getName() == "/"

class TestDirClass:
    def testName(self):
        root = fs.Dir("/")
        assert root.getName() == "/"

    def testAddDir(self):
        root = fs.Dir("/")
        fs.newDir(root, "newDir")
        assert root.getDir()[0].getName() == "newDir"

    def testAddFile(self):
        root = fs.Dir("/")
        fs.addNewFile(root, (1234, "file"))
        assert root.getFiles() == [(1234, "file")]
        assert root.getSize() == 1234
    
class TestFileExploration:
    def testParseLine(self):
        assert fs.parseLine("14848514 b.txt") == ("nf", (14848514, "b.txt"))
        assert fs.parseLine("$ ls") == None
        assert fs.parseLine("dir mew") == ("d", "mew")
    def testReadLineFromFile(self):
        fs.COMMANDS = fs.readFile("test_fileread.txt")
        assert fs.COMMANDS.nextLine() == "test 1\n"
        assert fs.COMMANDS.nextLine() == "test 2\n"
        fs.COMMANDS.close()

def test_main():
    assert fs.main("test_input.txt") == 95437