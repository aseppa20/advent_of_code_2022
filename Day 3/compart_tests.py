import pytest
import compart

###Part 1:

def test_cutInHalf():
    assert compart.cutInHalf("vJrwpWtwJgWrhcsFMMfFFhFp") == ("vJrwpWtwJgWr","hcsFMMfFFhFp")

def test_findDupes():
    assert compart.findDupes(("vJrwpWtwJgWr","hcsFMMfFFhFp")) == ['p']

def test_getLetterValue():
    assert compart.getLetterValue( compart.findDupes(("vJrwpWtwJgWr","hcsFMMfFFhFp"))[0] ) == 16

def test_main():
    assert compart.main("test_input.txt") == (157, 70)

###Part 2:

def test_findInGroup():
    assert compart.findCommonInGroup(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]) == 'r'