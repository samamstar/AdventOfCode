
data = []
with open("2024/prompts/2p.txt") as f:
    for line in f:
        splitLine = line.split()
        numLine = []
        for i in splitLine:
            numLine.append(abs(int(i)))
        data.append(numLine)

total = 0
for entry in data:
    entryOK = True
    if entry[0] > entry[1]:
        previousData = entry[0] + 1
        for dataPoint in entry:
            if previousData <= dataPoint:
                entryOK = False
            if previousData - dataPoint > 3:
                entryOK = False
            previousData = dataPoint
    else:
        previousData = entry[0] - 1
        for dataPoint in entry:
            if previousData >= dataPoint:
                entryOK = False
            if dataPoint - previousData > 3:
                entryOK = False
            previousData = dataPoint
    total += entryOK


print("Part1:", total)


def check(entry):
    if entry[0] > entry[1]:
        previousData = entry[0] + 1
        for index, dataPoint in enumerate(entry):
            if previousData <= dataPoint:
                return ((False))
            if previousData - dataPoint > 3:
                return ((False))
            previousData = dataPoint
    else:
        previousData = entry[0] - 1
        for index, dataPoint in enumerate(entry):
            if previousData >= dataPoint:
                return ((False))
            if dataPoint - previousData > 3:
                return ((False))
            previousData = dataPoint
    return ((True))


total = 0
for entry in data:
    if check(entry):
        total += 1
    else:
        for index, dataPoint in enumerate(entry):
            test = entry.copy()
            test.pop(index)
            if check(test):
                total+= 1
                break

print("Part2:", total)
