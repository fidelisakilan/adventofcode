import math

file = open("day17/input.txt", "r")

lines = file.readlines()

program = []
A = 0
B = 0
C = 0
IR = 0
length = 0


def combo(operand):
    if operand < 4:
        return operand
    return [A, B, C][operand - 4]


for line in lines:
    if line.startswith("Register A:"):
        A = int(line.split(":")[1].strip())
    elif line.startswith("Register B:"):
        B = int(line.split(":")[1].strip())
    elif line.startswith("Register C:"):
        C = int(line.split(":")[1].strip())
    elif line.startswith("Program:"):
        program = [int(item) for item in line.split(":")[1].strip().split(",")]
        program = list(zip(program[::2], program[1::2]))

length = len(program)

while IR < length:
    opcode, operand = program[IR]
    match opcode:
        case 0:
            A = int(A / 2 ** combo(operand))
        case 1:
            B = B ^ operand
        case 2:
            B = combo(operand) % 8
        case 3:
            if A != 0:
                IR = int(operand / 2)
                continue
        case 4:
            B = B ^ C
        case 5:
            out = combo(operand) % 8
            print(out, end=",")
        case 6:
            B = int(A / math.pow(2, combo(operand)))
        case 7:
            C = int(A / math.pow(2, combo(operand)))
    IR += 1
