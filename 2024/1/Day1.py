import fileinput

firstList = []
secondList = []
with open("/home/sam/Git/AdventOfCode/2024/prompt1.txt") as f:
    for line in f:
        splitLine = line.split()
        firstList.append(splitLine[0])
        secondList.append(splitLine[1])
firstList.sort()
secondList.sort()

total = 0
for i in range(0, len(firstList)):
    total += abs(int(firstList[i])-int(secondList[i]))
print("difference: " + str(total))

total = 0
for i in firstList:
    count = 0
    for j in secondList:
        if i == j:
            count += 1
    total += count * int(i)
print("Similarity: " + str(total))