def parse():
    keys = []
    locks = []
    with open("input/25.txt") as f:
        file = f.read()
    for code in file.split("\n\n"):
        counts = [-1 for _ in range(5)]
        if code[0] == ".":
            for line in code.split("\n"):
                index = 0
                for c in line:
                    if c == "#":
                        counts[index] += 1
                    index += 1
            keys.append(counts)
        if code[0] == "#":
            for line in code.split("\n"):
                index = 0
                for c in line:
                    if c == "#":
                        counts[index] += 1
                    index += 1
            locks.append(counts)
    return keys, locks


def p1():
    keys, locks = parse()
    valid_combinations = set()
    for lock in locks:
        for key in keys:
            index = 0
            is_valid = True
            while index != 5:
                if (5 - lock[index]) < key[index]:
                    is_valid = False
                    break
                index += 1
            if is_valid:
                valid_combinations.add((tuple(key), tuple(lock)))

p1()
