import pytest
import Calorie_calc

def test_findMax():
    assert Calorie_calc.findMax( [1, 2, 1] ) == 2

def test_readFile():
    assert Calorie_calc.readData("testdata.txt") == [2, 3, 5]

def test_findMaxTopThree():
    assert Calorie_calc.readData("testdata.txt") == [2, 3, 5]