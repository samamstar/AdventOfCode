grid = []
with open("2024/prompts/16p.txt") as f:
    for line in f:
        if line == "\n":
            break
        line = line.strip()
        line = list(line)
        grid.append(line)


def movePoint(point, direction):
    pointx = point[0]
    pointy = point[1]
    match direction:
        case 0:
            pointy -= 1
        case 1:
            pointx += 1
        case 2:
            pointy += 1
        case 3:
            pointx -= 1
    return (pointx, pointy)


def getPoint(point, grid):
    return grid[point[1]][point[0]]


def clockWise(direction):
    direction += 1
    direction = direction % 4
    return direction


def widershins(direction):
    direction -= 1
    direction = direction % 4
    return direction


def printGrid(grid):
    for line in grid:
        line = "".join(line)
        print(line)


def setPoint(point, val, grid):
    grid[point[1]][point[0]] = val


goal = (len(grid[0])-2, 1)
start = (1, len(grid)-2)
toCheck = [[(1, len(grid)-2), 1, 0]]
nodeScores = {start: 0}
nodeSteps = {start: 0}
while (len(toCheck)):
    current = toCheck.pop(0)
    point = current[0]
    currentScore = current[2]
    currentSteps = nodeSteps.get(point)

    # forward
    direction = current[1]
    nextPoint = movePoint(point, direction)
    nextScore = currentScore + 1
    if (nodeScores.get(nextPoint) == None or nodeScores.get(nextPoint) > nextScore) and getPoint(nextPoint, grid) != "#":
        nodeScores[nextPoint] = nextScore
        toCheck.append([nextPoint, direction, nextScore])
        nodeSteps[nextPoint] = currentSteps + 1

    # left
    direction = widershins(current[1])
    nextPoint = movePoint(point, direction)
    nextScore = currentScore + 1001
    if (nodeScores.get(nextPoint) == None or nodeScores.get(nextPoint) > nextScore) and getPoint(nextPoint, grid) != "#":
        nodeScores[nextPoint] = nextScore
        toCheck.append([nextPoint, direction, nextScore])
        nodeSteps[nextPoint] = currentSteps + 1

    # right
    direction = clockWise(current[1])
    nextPoint = movePoint(point, direction)
    nextScore = currentScore + 1001
    if (nodeScores.get(nextPoint) == None or nodeScores.get(nextPoint) > nextScore) and getPoint(nextPoint, grid) != "#":
        nodeScores[nextPoint] = nextScore
        toCheck.append([nextPoint, direction, nextScore])
        nodeSteps[nextPoint] = currentSteps + 1

print("Part1:", nodeScores.get((goal)))

toCheck = [goal]
countedPoints = []
while len(toCheck):
    check = toCheck.pop(0)
    if check in countedPoints:
        continue
    countedPoints.append(check)
    checkSteps = nodeSteps.get(check)

    # up
    nextPoint = (check[0], check[1]-1)
    nextSteps = nodeSteps.get(nextPoint)
    if (nextSteps != None and checkSteps > nextSteps):
        toCheck.append(nextPoint)

    # down
    nextPoint = (check[0], check[1]+1)
    nextSteps = nodeSteps.get(nextPoint)
    if (nextSteps != None and checkSteps > nextSteps):
        toCheck.append(nextPoint)

    # right
    nextPoint = (check[0]+1, check[1])
    nextSteps = nodeSteps.get(nextPoint)
    if (nextSteps != None and checkSteps > nextSteps):
        toCheck.append(nextPoint)

    # left
    nextPoint = (check[0]-1, check[1])
    nextSteps = nodeSteps.get(nextPoint)
    if (nextSteps != None and checkSteps > nextSteps):
        toCheck.append(nextPoint)

for point in sorted(nodeScores.keys()):
    setPoint(point, str(nodeScores.get(point))[0], grid)
    print(point,nodeScores.get(point))

for point in countedPoints:
    setPoint(point,"O",grid)

printGrid(grid)
print("part2:", len(countedPoints))
