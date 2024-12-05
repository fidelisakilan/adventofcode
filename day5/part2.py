file = open("input.txt", "r")
doc = file.readlines()

updates = []
rules = []
sum = 0

for line in doc:
    current_line = line.strip()
    if current_line == "":
        continue
    elif "|" in current_line:
        rules.append(tuple(current_line.split("|")))
    elif "," in current_line:
        updates.append(tuple(current_line.split(",")))


def check_update_validity(update):
    combinations = get_combinations(update)
    for i in combinations:
        if i[::-1] in rules:
            return False
    return True


def get_combinations(update):
    combinations = []
    for index1, i in enumerate(update):
        for index2, j in enumerate(update):
            if index1 != index2:
                combinations.append((i, j) if index1 < index2 else (j, i))
    return combinations


def get_ordered_update(update):
    ordered_update = [update[0]]

    for i in update[1:]:
        added = False
        j = 0
        while not added:
            if j == len(ordered_update):
                ordered_update.append(i)
                added = True
            elif (ordered_update[j], i) in rules or (
                i,
                ordered_update[j],
            ) not in rules:
                j = j + 1
            else:
                ordered_update.insert(j, i)
                added = True
    return ordered_update


for update in updates:
    result = check_update_validity(update)
    if result:
        # print(sum, result, update)
        # sum += int(update[int(len(update) / 2)])
        pass
    else:
        ordered_update = get_ordered_update(update)
        sum += int(ordered_update[int(len(ordered_update) / 2)])
        print(sum, result, ordered_update)
