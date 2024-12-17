
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
OUT A/2^B mod 8
Divide A by 8
Restart if A > 0
"""

# So what does this tell me?
# Unless B is zero on that out, then out will always be even?
# Because 2^B will always be... wait shit no that's just wrong
# Some of these operations are destructive, I don't think I can just run this backwards to get the original A
# Makes sense, there's multiple possible As for each output

# Hmm what if there are patterns in the binary...
# A of 55593699 is          011 010 100 000 100 101 011 100 011 (Added a leading zero to match length)
# Outputs 6,0,6,3,0,2,3,1,6 110 000 110 011 000 010 011 001 110
# OK so that means our final A result will need to be 16*3 = 48 bits (Well, 47 or 46 depending on leading zeroes)
# I don't think that works, because there's other patterns that don't hold

# A of 55593699 is          011 010 100 000 100 101 011 100 011 (Added a leading zero to match length)
# Output triplets reversed: 110 001 011 010 000 011 110 000 110 
# Still no dice. The 011s on the A match the 110s on the output, but 100 results in 000 or 011

# outString = "" 
# for outVal in reversed(output):
#     outString += "{:03b} ".format(outVal)
# print(outString)

# I think I need to solve this problem differently

finalA = 0
for outVal in reversed(program):
    finalA *= 8

    while(finalA):
        pass
    
print("Part2:", finalA)