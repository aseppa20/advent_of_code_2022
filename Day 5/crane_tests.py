import pytest
import crane

def test_buildStacks():
    crane.buildStacks("test_input.txt")
    assert crane.STACKS == [[],['N', 'Z'],['D', 'C', 'M'],['P'],[],[],[],[],[],[]]

def test_parseInstructions():
    assert crane.parseInstructions("move 1 from 2 to 1") == (1,2,1)

def test_executeInstructions():
    crane.executeInstructions( (1,2,1) )
    assert crane.STACKS == [[],['N', 'Z', 'M'],['D', 'C'],['P'],[],[],[],[],[],[]]

def test_readTops():
    assert crane.readTops() == "MCP"