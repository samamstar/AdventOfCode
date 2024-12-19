towels = set()
patterns = []
with open("2024/prompts/19p.txt") as f:
    for towel in f.__next__().strip().split(", "):
        towels.add(towel)
    f.__next__()
    for line in f:
        patterns.append(line.strip())

total = 0
for pattern in patterns:
    toCheck = towels.copy()
    while len(toCheck):
        candidate = toCheck.pop()
        if pattern[:len(candidate)] != candidate:
            continue
        if candidate == pattern:
            total += 1
            break
        for towel in towels:
            toCheck.add(candidate+towel)
print("Part1:", total)

# Oh god
# OK, concept: I can store towels with a list of towels that can combine to make that towel
# I think there's a datatype for stuff like this. A tree, maybe?
# If a towel will fit in, skip all its children, and then we can just add the number of combinations for the children...
# Wait no. That will skip combinations on the borders between big towels
# Might be workable: match a large towel in a pattern, and see if before and after work
# Lots of weird edge cases might come up with that tho
total = 0
for pattern in patterns:
    toCheck.clear()
    for towel in towels:
        toCheck.add((towel, towel))
    while len(toCheck):
        candidate = toCheck.pop()
        candidateString = candidate[0]
        if pattern[:len(candidateString)] != candidateString:
            continue
        if candidateString == pattern:
            total += 1
            print("Found", candidate)
            continue
        for towel in towels:
            toCheck.add((candidateString+towel,) + candidate[1:] + (towel,))
    print("done", pattern)
print("Part2:", total)
