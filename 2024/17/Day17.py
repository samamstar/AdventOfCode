
with open("2024/prompts/17p.txt") as f:
    regA = int(f.__next__().split()[2])
    regB = int(f.__next__().split()[2])
    regC = int(f.__next__().split()[2])
    f.__next__()
    program = []
    for opCode in f.__next__().split()[1].split(","):
        program.append(int(opCode))


def readCombo(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC


output = []
instructionPointer = 0
while (instructionPointer < len(program)):
    opCode = program[instructionPointer]
    instructionPointer += 1
    operand = program[instructionPointer]
    instructionPointer += 1

    match opCode:
        case 0:
            regA = int(regA/2**readCombo(operand))
        case 1:
            regB = regB ^ operand
        case 2:
            regB = readCombo(operand) % 8
        case 3:
            if regA != 0:
                instructionPointer = operand
        case 4:
            regB = regB ^ regC
        case 5:
            output.append(readCombo(operand) % 8)
        case 6:
            regB = int(regA/2**readCombo(operand))
        case 7:
            regC = int(regA/2**readCombo(operand))

# Thanks SO! I should learn list comprehension...
print("Part1:", ",".join([str(x) for x in output]))

# BST A
# BXL 3
# CDV B
# ADV 3
# BXL B
# BXC B
# OUT B
# JNZ 0

# in words:
"""
copy A mod 8 to B
XOR B with 011
Divide A by 2^B, store in C
Divide A by 8
Zero out B
Copy C to B
Out B
Restart if A > 0
"""

# simplify:
"""
Copy A mod 8 to B
XOR B with 011
OUT A/2^B
Divide A by 8
Restart if A > 0
"""

# So, work backwards, Sam.

finalA = 0
for outVal in reversed(program):
    finalA *= 8

    # Find the smallest B value that will output outVal (Hopefully always less than 8?)
    bVal = 0
    while(finalA/ 2**(bVal ^ 3) != outVal):
        bVal += 1
    
    finalA += bVal
print("Part2:", finalA)