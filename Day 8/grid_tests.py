import grid

def test_scanToInsertMinusOne():
    assert grid.scanToInsertMinusOneLeftToRight([1, 2, 3, 1, 0]) == [1, 2, 3, -1, -1]

def test_scanToInstertMinusOneUpToDown():
    assert grid.scanToInstertMinusOneUpToDown([[1, 2, 3, 4], [2, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]) == [[1, 2, 3, 4], [2, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]

def test_countVisibleTrees():
    assert grid.countVisibleTrees([[4, -3, 0, 20, 4], [-1, 8, 8, -4, -1], [24, 2, -4, 0, -1], [0, -4, 8, -4, 36], [4, 8, 0, 36, -2]]) == 21

def test_main():
    assert grid.main("test_input.txt") == (21, 8)

def test_countTrees():
    assert grid.countTreesToDown( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 3 ) == 1
    assert grid.countTreesToLeft( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 3 ) == 2
    assert grid.countTreesToRight( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 3 ) == 2
    assert grid.countTreesToUp( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 3 ) == 2

    assert grid.countTreesToDown( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 1 ) == 2
    assert grid.countTreesToLeft( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 1 ) == 1
    assert grid.countTreesToRight( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 1 ) == 2
    assert grid.countTreesToUp( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 2, 1 ) == 1

    assert grid.countTreesToDown( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 1, 1 ) == 1
    assert grid.countTreesToLeft( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 1, 1 ) == 1
    assert grid.countTreesToRight( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 1, 1 ) == 1
    assert grid.countTreesToUp( [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]], 1, 1 ) == 1