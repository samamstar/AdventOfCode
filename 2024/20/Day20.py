
def setPoint(point, val, grid):
    grid[point[1]][point[0]] = val


def printGrid(grid):
    for line in grid:
        line = "".join(line)
        print(line)


grid = []
with open("2024/prompts/20p.txt") as f:
    for line in f:
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


def isValidPoint(point, grid):
    if nextPoint[1] > len(grid) or nextPoint[0] > len(grid[0]):
        return False
    if nextPoint[1] < 0 or nextPoint[0] < 0:
        return False
    return True


for y in range(len(grid)):
    for x in range(len(grid[0])):
        if getPoint((x, y), grid) == "S":
            start = x, y
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if getPoint((x, y), grid) == "E":
            goal = x, y
toCheck = [start]
nodeScores = {start: 0}
# Generates a list of all valid (non-#) points and puts their distance from S into nodeScores
while (len(toCheck)):
    current = toCheck.pop(0)
    point = current
    currentScore = nodeScores.get(point)
    direction = 0

    for direction in range(0, 4):
        nextPoint = movePoint(point, direction)
        if nextPoint[1] > len(grid) or nextPoint[0] > len(grid[0]):
            continue
        if nextPoint[1] < 0 or nextPoint[0] < 0:
            continue
        nextScore = currentScore + 1
        if (nodeScores.get(nextPoint) == None or nodeScores.get(nextPoint) > nextScore) and getPoint(nextPoint, grid) != "#":
            nodeScores[nextPoint] = nextScore
            toCheck.append(nextPoint)


cheatResults = {}
transforms = ((-2, 0), (0, -2), (2, 0), (0, 2))
# For each node in nodeScores, checks the points 2 away in each cardinal direction for if it's a valid node, then checks if our cheat to get there actually saved time
for properStart in nodeScores.keys():
    for transform in transforms:
        cheatStart = (properStart[0]+transform[0], properStart[1]+transform[1])
        if nodeScores.get(cheatStart) == None:
            continue
        cheatScore = nodeScores.get(properStart) + 2
        if nodeScores.get(cheatStart) <= cheatScore:
            continue
        cheatSave = nodeScores.get(cheatStart) - cheatScore
        cheatResults[cheatSave] = cheatResults.get(
            cheatSave, []) + [(properStart, cheatSave)]

total = 0
for save in sorted(cheatResults.keys()):
    if save >= 100:
        total += len(cheatResults.get(save))
print("Part1:", total)


cheatResults = {}
transforms = []
for x in range (-20,21):
    for y in range (-20,21):
        if abs(x) + abs(y) > 20:
            continue
        transforms.append((x,y))

# Same as part 1's solution, but checks all points within the diamond reachable by a 20 step cheat
for properStart in nodeScores.keys():
    for transform in transforms:
        cheatStart = (properStart[0]+transform[0], properStart[1]+transform[1])
        if nodeScores.get(cheatStart) == None:
            continue
        cheatScore = nodeScores.get(properStart) + abs(transform[0]) + abs(transform[1])
        if nodeScores.get(cheatStart) <= cheatScore:
            continue
        cheatSave = nodeScores.get(cheatStart) - cheatScore
        cheatResults[cheatSave] = cheatResults.get(
            cheatSave, []) + [(properStart, cheatSave)]
    print("checked",properStart)

total = 0
for save in sorted(cheatResults.keys()):
    if save >= 100:
        total += len(cheatResults.get(save))
print("Part2:", total)