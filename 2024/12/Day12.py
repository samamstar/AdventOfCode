with open("2024/prompts/12p.txt") as f:
    map = []
    for line in f.readlines():
        line = line.strip()
        map.append([letter for letter in line])

checked = set()


# Stefan says recursion is bad. Doesn't work in part 2 (For good reason)
def checkPoint(region, x, y, shouldBe):
    if (x, y) in checked:
        return
    if map[y][x] != shouldBe:
        return
    checked.add((x, y))
    region.append((x, y))
    if x > 0:
        checkPoint(region, x - 1, y, shouldBe)
    if y > 0:
        checkPoint(region, x, y - 1, shouldBe)
    if y < len(map)-1:
        checkPoint(region, x, y+1, shouldBe)
    if x < len(map[0])-1:
        checkPoint(region, x + 1, y, shouldBe)


regions = []
for y, line in enumerate(map):
    for x, item in enumerate(line):
        if (x, y) in checked:
            continue
        region = []
        checkPoint(region, x, y, item)
        regions.append(region)

total = 0
for region in regions:
    perimeter = 0
    for point in region:
        if not (point[0], point[1]+1) in region:
            perimeter += 1
        if not (point[0]+1, point[1]) in region:
            perimeter += 1
        if not (point[0]-1, point[1]) in region:
            perimeter += 1
        if not (point[0], point[1]-1) in region:
            perimeter += 1
    total += perimeter*len(region)
print("Part1:", total)


def pointInDirection(x, y, direction):
    if direction == 0:
        return (x, y-1)
    if direction == 1:
        return (x+1, y)
    if direction == 2:
        return (x, y+1)
    if direction == 3:
        return (x-1, y)


def getRegionSides(region):
    sides = 0
    startPoint = region[0]
    direction = 1
    x = region[0][0]
    y = region[0][1]
    while True:
        if (pointInDirection(x, y, (direction - 1) % 4) in region):
            direction = (direction-1) % 4
            sides += 1
            x = pointInDirection(x, y, direction)[0]
            y = pointInDirection(x, y, direction)[1]
        elif pointInDirection(x, y, direction) in region:
            x = pointInDirection(x, y, direction)[0]
            y = pointInDirection(x, y, direction)[1]
        else:
            direction = (direction+1) % 4
            sides += 1
            if direction == 1 and (x, y) == startPoint:
                break
    return sides


def findInteriorRegions(outerRegion):
    newRegions = []
    checked = set()
    for point in outerRegion:
        checked.add(point)

    for y in range(len(map)):
        for x in range(len(map[0])):
            search = [(x,y)]
            isInterior = True
            newRegion = []
            while len(search)>0:
                point = search.pop()
                if point in checked:
                    continue
                checked.add(point)
                newRegion.append(point)
                pointx = point[0]
                pointy = point[1]
                if pointx > 0:
                    search.append((pointx-1,pointy))
                else:
                    isInterior = False
                if pointx < len(map[0])-1:
                    search.append((pointx+1,pointy))
                else:
                    isInterior = False
                if pointy > 0:
                    search.append((pointx,pointy-1))
                else:
                    isInterior = False
                if pointy < len(map)-1:
                    search.append((pointx,pointy+1))
                else:
                    isInterior = False
            if len(newRegion) > 0 and isInterior:
                newRegions.append(newRegion)
    return newRegions


total = 0
for region in regions:
    sides = getRegionSides(region)
    for interiorRegion in findInteriorRegions(region):
        sides += getRegionSides(interiorRegion)
    total += sides * len(region)
print("Part2:", total)
