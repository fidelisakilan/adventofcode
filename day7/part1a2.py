file = open("input.txt", "r")

test_values = []
operand_list = []

for line in file.readlines():
    test_values.append(int(line.strip().split(":")[0]))
    items = (line.strip().split(":")[1]).strip().split(" ")
    operand_list.append(list(map(int, items)))

index = 0
count = 0
length = len(test_values)


def generate_combinations(current, depth, result):
    if depth == 0:
        result.append(tuple(current))
        return
    for value in [0, 1, 2]:
        generate_combinations(current + [value], depth - 1, result)


def calculate(operators, operands):
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == 0:
            result = result * operands[i + 1]
        if operators[i] == 1:
            result = result + operands[i + 1]
        if operators[i] == 2:
            result = int(str(result) + str(operands[i + 1]))
        operators[i]
    return result


def test_operands(test, operands):
    combinations = []
    generate_combinations([], len(operands) - 1, combinations)
    for operators in combinations:
        result = calculate(operators, operands)
        if result == test:
            return True
    return False


for i in range(length):
    result = test_operands(test_values[i], operand_list[i])
    if result:
        count += test_values[i]
    print(f"{i}/{length}", result)
print(count)
