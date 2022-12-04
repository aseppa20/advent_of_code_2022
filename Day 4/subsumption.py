def checkSubsumption(tasksA: tuple, tasksB: tuple, flipped=False) -> bool:
    if int(tasksA[0]) <= int(tasksB[0]) and int(tasksA[1]) >= int(tasksB[1]):
        return True
    
    if not flipped:
        return checkSubsumption(tasksB, tasksA, True)

    return False


def checkOverlap(tasksA: tuple, tasksB: tuple, flipped=False) -> bool:
    if int(tasksA[0]) <= int(tasksB[0]) and int(tasksB[0]) <= int(tasksA[1]):
        return True

    if int(tasksB[0]) <= int(tasksA[1]) and int(tasksA[1]) <= int(tasksB[1]):
        return True

    if not flipped:
        return checkOverlap(tasksB, tasksA, True)

    return False


def main(filename="input.txt"):
    
    counterSub = 0
    counterOverlap = 0

    with open(filename, "r") as file:
        for line in file.readlines():
            pair = str(line).split(',')
            mainTasksA = pair[0].split('-')
            mainTasksB = pair[1].split('-')

            if checkSubsumption(tuple(mainTasksA), tuple(mainTasksB)):
                counterSub += 1
                counterOverlap += 1
            elif checkOverlap(tuple(mainTasksA), tuple(mainTasksB)):
                counterOverlap += 1

    print(f"{counterSub} , {counterOverlap}")
    return (counterSub , counterOverlap)


if __name__ == "__main__":
    main()