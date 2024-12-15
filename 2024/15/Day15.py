grid = []
commands = []
with open("2024/prompts/15ps.txt") as f:
    for line in f:
        if line == "\n":
            break
        line = line.strip()
        line = list(line)
        grid.append(line)
    for line in f:
        line = line.strip()
        commands += list(line)

grid2 = []
for line in grid:
    newLine = []
    for point in line:
        match point:
            case "#":
                newLine.append("#")
                newLine.append("#")
            case "O":
                newLine.append("[")
                newLine.append("]")
            case ".":
                newLine.append(".")
                newLine.append(".")
            case "@":
                newLine.append("@")
                newLine.append(".")
    grid2.append(newLine)


def printGrid(grid):
    for line in grid:
        line = "".join(line)
        print(line)


width = len(grid[0])
height = len(grid)
for x in range(0, width):
    for y in range(0, height):
        if grid[y][x] == "@":
            botPos = [x, y]


def movePoint(point, direction):
    result = point.copy()
    match direction:
        case 0:
            result[1] -= 1
        case 1:
            result[0] += 1
        case 2:
            result[1] += 1
        case 3:
            result[0] -= 1
    return result


def getPoint(point, grid):
    return grid[point[1]][point[0]]


def setPoint(point, val, grid):
    grid[point[1]][point[0]] = val


for command in commands:
    match command:
        case "^":
            direction = 0
        case ">":
            direction = 1
        case "v":
            direction = 2
        case "<":
            direction = 3
    checkPoint = botPos.copy()
    while not getPoint(checkPoint, grid) == "#" and not getPoint(checkPoint, grid) == ".":
        checkPoint = movePoint(checkPoint, direction)
    if getPoint(checkPoint, grid) == "#":
        continue
    backwards = (direction+2) % 4
    while getPoint(checkPoint, grid) != "@":
        setPoint(checkPoint, "O", grid)
        checkPoint = movePoint(checkPoint, backwards)
    setPoint(movePoint(checkPoint, direction), "@", grid)
    setPoint(checkPoint, ".", grid)
    botPos = movePoint(botPos, direction)

total = 0
for x in range(width):
    for y in range(height):
        if getPoint([x, y], grid) == "O":
            total += 100 * y
            total += x
print("part1:", total)

width = len(grid2[0])
height = len(grid2)
for x in range(0, width):
    for y in range(0, height):
        if grid2[y][x] == "@":
            botPos = [x, y]

for command in commands:
    printGrid(grid2)
    match command:
        case "^":
            direction = 0
        case ">":
            direction = 1
        case "v":
            direction = 2
        case "<":
            direction = 3
    checkPoints = [botPos.copy()]
    bonked = False
    shiftPoints = []
    while True:
        clear = True
        for i, checkPoint in enumerate(checkPoints):
            shiftPoints.append((checkPoint, getPoint(checkPoint, grid2)))
            nextPoint = movePoint(checkPoint, direction)
            nextVal = getPoint(nextPoint, grid2)
            checkPoints[i] = nextPoint
            if nextVal == "#":
                bonked = True
                break
            if direction == 0 or direction == 2:
                if nextVal == "[":
                    if not movePoint(nextPoint, 1) in checkPoints:
                        checkPoints.append(movePoint(nextPoint, 1))
                if nextVal == "]":
                    if not movePoint(nextPoint, 3) in checkPoints:
                        checkPoints.append(movePoint(nextPoint, 3))
            if not nextVal == ".":
                clear = False
        if bonked or clear:
            break
    if bonked == True:
        continue
    backwards = (direction+2) % 4
    for pointInfo in shiftPoints:
        setPoint(movePoint(pointInfo[0], direction), pointInfo[1], grid2)
        if pointInfo[0][1] == botPos[1] and direction in [0,2]:
            setPoint(pointInfo[0], ".", grid2)
    setPoint(botPos,".",grid2)
    botPos = movePoint(botPos, direction)
