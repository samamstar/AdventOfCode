import re

with open("2024/prompts/3p.txt") as f:
    stream = f.read()

total = 0
for command in re.findall(r"mul\(\d+,\d+\)", stream):
    numbers = re.findall(r"\d+", command)
    total += int(numbers[0]) * int(numbers[1])
print("Part1:", total)

total = 0
mulOn = True
for command in re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", stream):
    if(command == "don't()"):
        mulOn = False
    elif(command == "do()"):
        mulOn = True
    elif(mulOn):
        numbers = re.findall(r"\d+", command)
        total += int(numbers[0]) * int(numbers[1])
print("Part2:", total)