def XOR(a, b):
    return a != b


def AND(a, b):
    return a == 1 and b == 1


def OR(a, b):
    return a == 1 or b == 1


def parse():
    wires = {}
    connections = []
    with open("input/24.txt") as f:
        file = f.read().strip()

    wires_str = file.split("\n\n")[0]
    connections_str = file.split("\n\n")[1]
    for s in wires_str.split("\n"):
        key, value = s.split(": ")
        wires[key] = int(value)

    for s in connections_str.split("\n"):
        p1, op, p2, _, output = s.split(" ")
        connections.append((p1, op, p2, output))
    return wires, connections


def getxy(wires):
    xs = sorted(filter(lambda x: x[0] == "x", wires.keys()), reverse=True)
    ys = sorted(filter(lambda y: y[0] == "y", wires.keys()), reverse=True)
    xs = "".join(map(lambda x: str(wires[x]), xs))
    ys = "".join(map(lambda y: str(wires[y]), ys))
    return int(xs, 2), int(ys, 2)


def p1():
    wires, connections = parse()
    while len(connections) != 0:
        p1, op, p2, out = connections.pop(0)
        if p1 in wires and p2 in wires:
            p1, p2 = wires[p1], wires[p2]
            result = 0
            match op:
                case "OR":
                    result = OR(p1, p2)
                case "XOR":
                    result = XOR(p1, p2)
                case "AND":
                    result = AND(p1, p2)
            wires[out] = 1 if result is True else 0
        else:
            connections.append((p1, op, p2, out))
    counter = 0
    binary_number = ""
    while f"z{counter:0>2}" in wires:
        binary_number = str(wires[f"z{counter:0>2}"]) + binary_number
        counter += 1
    print(binary_number)
    print(int(binary_number, 2))


def p2():
    pass


# p1()
p2()
