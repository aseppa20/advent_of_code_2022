import rps
import pytest

def test_rps_equals():
    assert rps.rps( [1, 1] ) == 4 #Rock
    assert rps.rps( [2, 2] ) == 5 #Paper
    assert rps.rps( [3, 3] ) == 6 #Scissors

def test_rps_losing():
    assert rps.rps( [1, 3] ) == 3
    assert rps.rps( [2, 1] ) == 1
    assert rps.rps( [3, 2] ) == 2

def test_rps_winning():
    assert rps.rps( [3, 1] ) == 7
    assert rps.rps( [1, 2] ) == 8
    assert rps.rps( [2, 3] ) == 9

def test_strategy_translate():
    assert rps.translateStrategy( ['A', 'Z'] ) == [1, 3]
    assert rps.translateStrategy( ['B', 'X'] ) == [2, 1]
    assert rps.translateStrategy( ['C', 'Y'] ) == [3, 2]

def test_strategy_translateBetter():
    assert rps.translateStrategyBetter( ['A', 'Z'] ) == [1, 2]
    assert rps.translateStrategyBetter( ['B', 'X'] ) == [2, 1]
    assert rps.translateStrategyBetter( ['C', 'Y'] ) == [3, 3]

def test_main():
    score = 0
    score += rps.rps( rps.translateStrategyBetter( ['A', 'Y'] ) )
    assert score == 4
    score += rps.rps( rps.translateStrategyBetter( ['B', 'X'] ) )
    assert score == 5
    score += rps.rps( rps.translateStrategyBetter( ['C', 'Z'] ) ) 
    assert score == 12