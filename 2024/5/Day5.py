
from functools import cmp_to_key

with open("2024/prompts/5p.txt") as f:
    inputs = f.read().split("\n\n")
    rules = {}
    for rule in inputs[0].split():
        rule = rule.split("|")
        if not rules.get(int(rule[1])):
            rules[int(rule[1])] = []
        rules[int(rule[1])].append(int(rule[0]))
    books = []
    for book in inputs[1].split():
        book = book.split(",")
        for index, page in enumerate(book):
            book[index] = int(page)
        books.append(book)

total = 0
wrongBooks = []
for book in books:
    isOK = True
    seen = []
    for page in book:
        seen.append(page)
        if page in rules.keys():
            for checkPage in rules.get(page):
                if checkPage not in book:
                    continue
                if checkPage not in seen:
                    isOK = False
                    wrongBooks.append(book)
                    break
        if not isOK:
            break
    if isOK:
        total += book[int(len(book)/2)]
print("part1:", total)

# key > value
def compare(item1, item2):
    if item2 in rules.get(item1):
        return 1
    return -1
total = 0
for book in wrongBooks:
    total += sorted(book,key=cmp_to_key(compare))[int(len(book)/2)]

print("part2:", total)
