import numpy as np
import copy

def scanToInsertMinusOneLeftToRight(row) -> list:
    
    currentMax = -1

    for index, num in enumerate(row):
        if num > currentMax:
            currentMax = num
        else:
            row[index] = -1
    
    return row


def scanToInstertMinusOneUpToDown(matrix) -> list:
    columnLen = len(matrix)
    
    for col in range( len(matrix[0]) ):
        currentMax = -1
        for index in range(columnLen):
            if matrix[index][col] > currentMax:
                currentMax = matrix[index][col]
            else:
                matrix[index][col] = -1

    return matrix


def countVisibleTrees(matrix) -> int:
    count = 0
    
    for row in matrix:
        for num in row:
            if num != -4:
                count += 1
    
    return count


def countTreesToLeft( matrix, x, y ) -> int:
    #columnRow = len(matrix[0])
    count = 0
    seedsize = matrix[y][x]
    x -= 1
    
    while x >= 0:
        count += 1
        if matrix[y][x] >= seedsize:
            break
        x -= 1

    return count

def countTreesToRight( matrix, x, y ) -> int:
    rowLen = len(matrix[0]) - 1
    count = 0
    seedsize = matrix[y][x]
    x += 1

    while rowLen >= x:
        count += 1
        if matrix[y][x] >= seedsize:
            break
        x += 1
            
    return count

def countTreesToUp( matrix, x, y ) -> int:
    #columnLen = len(matrix)
    count = 0
    seedsize = matrix[y][x]
    y -= 1
    while y >= 0:
        count += 1
        if matrix[y][x] >= seedsize:
            break
        y -= 1

    return count

def countTreesToDown( matrix, x, y ) -> int:
    columnLen = len(matrix) - 1
    count = 0
    seedsize = matrix[y][x]
    y += 1

    while columnLen >= y:    
        count += 1
        if matrix[y][x] >= seedsize:
            break
        y += 1
            
    return count


def main(filename="input.txt"):
    matrix = []
    

    with open(filename, "r") as file:
        for index, line in enumerate(file.readlines()):
            line = line.strip()
            matrix.append([])
            for char in line:
                matrix[index].append(int(char))
        
        file.close()
    
    #print(matrix)
    matrixPart2 = copy.deepcopy(matrix)

    matrixLeftToRight = copy.deepcopy(matrix)
    matrixRightToLeft = copy.deepcopy(matrix)

    matrixUpToDown = copy.deepcopy(matrix)
    matrixDownToUp = copy.deepcopy(matrix) #-> reverse matrixUpToDown scan reverse result

    for row in matrixLeftToRight:
        row = scanToInsertMinusOneLeftToRight(row)
    
    for row in matrixRightToLeft:
        row.reverse()
        row = scanToInsertMinusOneLeftToRight(row)
        row.reverse()

    matrixUpToDown = scanToInstertMinusOneUpToDown(matrixUpToDown)

    matrixDownToUp.reverse()
    matrixDownToUp = scanToInstertMinusOneUpToDown(matrixDownToUp)
    matrixDownToUp.reverse()

    matrix = np.array( np.add( np.add(matrixLeftToRight, matrixRightToLeft) , np.add(matrixUpToDown, matrixDownToUp) ))

    visible = countVisibleTrees(matrix.tolist())

    maxScore = 0

    for iY, matrixY in enumerate(matrixPart2):
        for iX, matrixX in enumerate(matrixY):
            countUp = countTreesToUp(matrixPart2, iX, iY)
            countDown = countTreesToDown(matrixPart2, iX, iY)
            countLeft = countTreesToLeft(matrixPart2, iX, iY)
            countRight = countTreesToRight(matrixPart2, iX, iY)

            score = countUp * countDown * countLeft * countRight
            if score > maxScore:
                maxScore = int(score)
    
    return (visible, maxScore)


if __name__ == "__main__":
    print(main())
