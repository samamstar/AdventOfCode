
from functools import cmp_to_key

towels = set()
patterns = []
with open("2024/prompts/19ps.txt") as f:
    for towel in f.__next__().strip().split(", "):
        towels.add(towel)
    f.__next__()
    for line in f:
        patterns.append(line.strip())

# total = 0
# for pattern in patterns:
#     toCheck = towels.copy()
#     while len(toCheck):
#         candidate = toCheck.pop()
#         if pattern[:len(candidate)] != candidate:
#             continue
#         if candidate == pattern:
#             total += 1
#             break
#         for towel in towels:
#             toCheck.add(candidate+towel)
# print("Part1:", total)

# Oh god
# OK, concept: I can store towels with a list of towels that can combine to make that towel
# I think there's a datatype for stuff like this. A tree, maybe?
# If a towel will fit in, skip all its children, and then we can just add the number of combinations for the children...
# Wait no. That will skip combinations on the borders between big towels, right?
# Might be workable: match a large towel in a pattern, and see if before and after work
# Lots of weird edge cases might come up with that tho

# Brain blast: Use a set to squash possible outputs? Hmm the taste I got of workable solutions implies 300+ per pattern, but that's probably not so bad

# OK wait: algo idea:
# For each check, start the towels longest to shortest
# If we match, add all towels that combine into that towel FROM THE FIRST INDEX
# Continue as normal
# Possible combinations should be added to a set because I don't trust myself not to do redundant work so that will squash duplicates
# Total can be tallied at end
# This of course, totally skips the actual creation of the object that stores this. It's probably a tree
# I don't think this is close to optimal but it should be a lot faster than my naive approach

# Upon actually wrighting the first part (Making the dictionary), I'm less certain this will work at all

total = 0
toCheck = set()
toSkip = set()
toTally = set()
towelInfo = {}
for mainTowel in towels:
    combinations = set()
    skippable = set()
    for towel in towels:
        if towel != mainTowel:
            toCheck.add((towel,))
    while len(toCheck):
        candidate = toCheck.pop()
        candidateString = "".join(candidate)
        if mainTowel[:len(candidateString)] != candidateString:
            continue
        if candidateString == mainTowel:
            combinations.add(candidate)
            continue
        for towel in towels:
            toCheck.add(candidate + (towel,))
    for towel in combinations:
        skippable.add(towel[0])
    towelInfo[mainTowel] = (skippable, combinations)

# I wrote that lambda without checking SO at all! (W3 schools, on the other hand...)
sortedTowels = sorted(list(towels),key=cmp_to_key(lambda a,b:len(b) - len(a)))
print(sortedTowels)
for pattern in patterns:
    toCheck.clear()
    for towel in towels:
        toCheck.add((towel,))
    while len(toCheck):
        candidate = toCheck.pop()
        candidateString = "".join(candidate)
        if pattern[:len(candidateString)] != candidateString:
            continue
        if candidateString == pattern:
            total += 1
            print("Found", candidate, total, len(toCheck))
            continue
        for towel in sortedTowels:
            toCheck.add(candidate + (towel,))
    print("done", pattern)
print("Part2:", total)
