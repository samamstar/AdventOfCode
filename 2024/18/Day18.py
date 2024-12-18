
def setPoint(point, val, grid):
    grid[point[1]][point[0]] = val


def printGrid(grid):
    for line in grid:
        line = "".join(line)
        print(line)


grid = []
for i in range(0, 71):
    grid.append(["."]*71)

currentByte = 0
bytes = []
with open("2024/prompts/18p.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        bytes.append((int(line[0]), int(line[1])))

for i in range(0, 1024):
    currentByte += 1
    byte = bytes.pop(0)
    setPoint(byte, "#", grid)


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


goal = (70, 70)
start = (0, 0)
toCheck = [start]
nodeScores = {start: 0}
while (len(toCheck)):
    current = toCheck.pop(0)
    point = current
    currentScore = nodeScores.get(point)
    direction = 0

    for direction in range(0, 4):
        nextPoint = movePoint(point, direction)
        if nextPoint[1] > 70 or nextPoint[0] > 70:
            continue
        if nextPoint[1] < 0 or nextPoint[0] < 0:
            continue
        nextScore = currentScore + 1
        if (nodeScores.get(nextPoint) == None or nodeScores.get(nextPoint) > nextScore) and getPoint(nextPoint, grid) != "#":
            nodeScores[nextPoint] = nextScore
            toCheck.append(nextPoint)

print("Part1:", nodeScores.get(goal))

while nodeScores.get(goal) != None:
    currentByte += 1
    byte = bytes.pop(0)
    setPoint(byte, "#", grid)
    toCheck = [start]
    nodeScores = {start: 0}
    while (len(toCheck)):
        current = toCheck.pop(0)
        point = current
        currentScore = nodeScores.get(point)
        direction = 0
        for direction in range(0, 4):
            nextPoint = movePoint(point, direction)
            if nextPoint[1] > 70 or nextPoint[0] > 70:
                continue
            if nextPoint[1] < 0 or nextPoint[0] < 0:
                continue
            nextScore = currentScore + 1
            if (nodeScores.get(nextPoint) == None or nodeScores.get(nextPoint) > nextScore) and getPoint(nextPoint, grid) != "#":
                nodeScores[nextPoint] = nextScore
                toCheck.append(nextPoint)


print("Part2:", byte)