with open("2024/prompts/7p.txt") as f:
    data = []
    for line in f:
        line = line.split()
        line[0] = line[0].replace(":", "")
        dataLine = [int(line[0]), []]
        for i in range(1, len(line)):
            dataLine[1].append(int(line[i]))
        data.append(dataLine)

total = 0
for line in data:
    target = line[0]
    values = line[1]
    mask = 0b0
    while mask <= (0b1 << (len(values))):
        result = values[0]
        for i in range(1, len(values)):
            if (mask & (0b1 << i)):
                result *= values[i]
            else:
                result += values[i]
        if result == target:
            total += target
            break
        mask += 1
print("Part1:", total)

# HAH! Knew they'd have a third operator

total = 0
for line in data:
    target = line[0]
    values = line[1]
    mask = 0
    while mask <= (3 * len(values)):
        result = values[0]
        for i in range(1, len(values)):
            i -= 1
            if (int(mask/(3*i))%3 == 0):
                result *= values[i]
            if (int(mask/(3*i))%3 == 1):
                result += values[i]
            if (int(mask/(3*i))%3 == 2):
                result = int(str(result)+str(values[i]))
        if result == target:
            total += target
            break
        mask += 1
print("Part2:",total)