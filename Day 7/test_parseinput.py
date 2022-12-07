import parseinput

def test_parseInput():
    assert parseinput.parseLine("14848514 b.txt") == '14848514'
    assert parseinput.parseLine("$ cd ..") == ".."
    assert parseinput.parseLine("$ cd d") == "d"
    assert parseinput.parseLine("$ ls") == None
    assert parseinput.parseLine("dir mew") == None

def test_main():
    assert parseinput.main("test_input.txt") == (95437, 24933642)