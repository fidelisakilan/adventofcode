file = open("input.txt", "r")
doc = file.readlines()

updates = []
rules = []

for line in doc:
    current_line = line.strip()
    if current_line == "":
        continue
    elif "|" in current_line:
        rules.append(tuple(current_line.split("|")))
    elif "," in current_line:
        updates.append(tuple(current_line.split(",")))


def check_update_validity(combinations):
    for i in combinations:
        if i[::-1] in rules:
            return False
    return True


sum = 0
for update in updates:
    combinations = []
    for index1, i in enumerate(update):
        for index2, j in enumerate(update):
            if index1 != index2:
                combinations.append((i, j) if index1 < index2 else (j, i))
    result = check_update_validity(combinations)
    if result:
        sum += int(update[int(len(update) / 2)])
    print(sum, result, update)
