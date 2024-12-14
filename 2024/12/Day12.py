with open("2024/prompts/12p.txt") as f:
    map = []
    for line in f.readlines():
        line = line.strip()
        map.append([letter for letter in line])

checked = set()


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


# Returns false if invalid interior region (Ran into edge of map)
def checkInteriorPoint(region, x, y, checked, foundOutside, bounds):
    if (x, y) in checked:
        return
    checked.add((x, y))
    region.append((x, y))
    if x == bounds.get("minx") or y == bounds.get("miny") or y == bounds.get("maxy") or x == bounds.get("maxx"):
        foundOutside[0] = True
    if y > bounds.get("miny"):
        checkInteriorPoint(region, x, y - 1, checked,
                           foundOutside, bounds)
    if x > bounds.get("minx"):
        checkInteriorPoint(region, x - 1, y, checked,
                           foundOutside, bounds)
    if y < bounds.get("maxy"):
        checkInteriorPoint(region, x, y+1, checked,
                           foundOutside, bounds)
    if x < bounds.get("maxx"):
        checkInteriorPoint(region, x + 1, y, checked,
                           foundOutside, bounds)

def findBoundaryPoints(region):
    minx = region[0][0]
    maxx = region[0][0]
    miny = region[0][1]
    maxy = region[0][1]
    for point in region:
        if point[0] < minx:
            minx = point[0]
        if point[0] > maxx:
            maxx = point[0]
        if point[1] < miny:
            miny = point[0]
        if point[1] > maxy:
            maxy = point[0]
    result = {}
    result["minx"] = minx
    result["miny"] = miny
    result["maxx"] = maxx
    result["maxy"] = maxy
    return result


def findInteriorRegions(outerRegion):
    regions = []
    checked = set()
    for point in outerRegion:
        checked.add(point)

    bounds = findBoundaryPoints(outerRegion)
    for y in range(bounds.get("miny"), bounds.get("maxy")):
        for x in range(bounds.get("minx"), bounds.get("maxx")):
            if (x, y) in checked:
                continue
            newRegion = []
            foundOutside = [False]
            checkInteriorPoint(newRegion, x, y, checked,
                               foundOutside, bounds)
            if not foundOutside[0]:
                regions.append(newRegion)
                print("Found interior region of size", len(newRegion))
    return regions


total = 0
for region in regions:
    sides = getRegionSides(region)
    for interiorRegion in findInteriorRegions(region):
        sides += getRegionSides(interiorRegion)
    total += sides * len(region)
print("Part2:", total)
