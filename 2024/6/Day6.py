
with open("2024/prompts/6p.txt") as f:
    map = []
    for line in f.readlines():
        line = line.strip()
        map.append([letter for letter in line])

for y, line in enumerate(map):
    for x, spot in enumerate(line):
        if spot == "^":
            break
    if spot == "^":
        break
startX = x
startY = y
direction = 0  # 0,1,2,3 N,E,S,W
maxY = len(map) - 1
maxX = len(map[0]) - 1
while (True):
    map[y][x] = "X"
    match direction:
        case 0:
            nextX = x
            nextY = y-1
        case 1:
            nextX = x+1
            nextY = y
        case 2:
            nextX = x
            nextY = y+1
        case 3:
            nextX = x-1
            nextY = y
    if nextX > maxX or nextY > maxY or nextY < 0 or nextX < 0:
        break
    
    if map[nextY][nextX] == "#":
        direction += 1
        direction = direction % 4
        continue
    x = nextX
    y = nextY
total = 0
for line in map:
    for spot in line:
        if spot == "X":
            total += 1
print("Part1:", total)

with open("2024/prompts/6p.txt") as f:
    map = []
    for line in f.readlines():
        line = line.strip()
        map.append([letter for letter in line])
startMap = map
total = 0
for testy, line in enumerate(startMap):
    for testx, spot in enumerate(line):
        if not (spot == "." or spot == "X"):
            continue
        x = startX
        y = startY
        direction = 0
        startMap[testy][testx] = "#"
        stepsTaken = 0
        while (True):
            stepsTaken += 1
            match direction:
                case 0:
                    nextX = x
                    nextY = y-1
                case 1:
                    nextX = x+1
                    nextY = y
                case 2:
                    nextX = x
                    nextY = y+1
                case 3:
                    nextX = x-1
                    nextY = y
            if nextX > maxX or nextY > maxY or nextY < 0 or nextX < 0:
                break
            if stepsTaken > 10000: # fuck it
                total += 1
                break
            if startMap[nextY][nextX] == "#":
                direction += 1
                direction = direction % 4
                continue
            x = nextX
            y = nextY
        startMap[testy][testx] = "."
print("Part2:", total)
