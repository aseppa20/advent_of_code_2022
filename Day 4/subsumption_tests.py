import pytest
import subsumption

def test_checkSubsumption():
    assert subsumption.checkSubsumption( (6,6) , (4,6) ) == True
    assert subsumption.checkSubsumption( (4,6) , (6,6) ) == True
    assert subsumption.checkSubsumption( (6,6) , (6,6) ) == True
    assert subsumption.checkSubsumption( (2,4) , (6,8) ) == False
    assert subsumption.checkSubsumption( (2,4) , (3,8) ) == False

def test_checkOverlap():
    assert subsumption.checkOverlap( (6,6) , (4,6) ) == True
    assert subsumption.checkOverlap( (4,6) , (6,6) ) == True
    assert subsumption.checkOverlap( (6,6) , (6,6) ) == True
    assert subsumption.checkOverlap( (2,4) , (3,8) ) == True
    assert subsumption.checkOverlap( (5,7) , (7,9) ) == True
    assert subsumption.checkOverlap( (7,9) , (5,7) ) == True
    assert subsumption.checkOverlap( (2,4) , (6,8) ) == False

def test_main():
    assert subsumption.main("test_input.txt") == (2, 4)