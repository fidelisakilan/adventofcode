file = open("day15/input.txt", "r").read().split("\n\n")

sections = file
warehouse_section = sections[0]
directions_section = sections[1]


warehouse = [list(line) for line in warehouse_section.split("\n")]
directions = list(directions_section.replace("\n", ""))
r = len(warehouse)
c = len(warehouse[0])
si, sj = 0, 0
for i in range(r):
    for j in range(c):
        if warehouse[i][j] == "@":
            si, sj = i, j

# print(warehouse)
# print(directions)


def swap_positions(pending):
    global si, sj
    while len(pending) > 0:
        item = pending.pop()
        fromi, fromj = item[0]
        toi, toj = item[1]
        warehouse[toi][toj] = warehouse[fromi][fromj]
        warehouse[fromi][fromj] = "."
        if warehouse[toi][toj] == "@":
            si, sj = toi, toj


def print_matrix():
    for row in range(r):
        for col in range(c):
            print(warehouse[row][col], end=" ")
        print()


print_matrix()
for dir in directions:
    offsetx, offsety = 0, 0
    if dir == "<":
        offsetx, offsety = -1, 0
    elif dir == ">":
        offsetx, offsety = 1, 0
    elif dir == "^":
        offsetx, offsety = 0, -1
    elif dir == "v":
        offsetx, offsety = 0, 1
    movable = False
    pending = []
    ni, nj = si, sj
    while True:
        di, dj = ni + offsety, nj + offsetx
        next_item = warehouse[di][dj]
        if next_item == "#":
            pending = []
            break
        elif next_item == ".":
            pending.append([(ni, nj), (di, dj)])
            break
        elif next_item == "O":
            pending.append([(ni, nj), (di, dj)])
        ni, nj = di, dj
    swap_positions(pending)
    # print("\nMove", dir, ": ")
    # print_matrix()

sum = 0
for row in range(r):
    for col in range(c):
        if warehouse[row][col] == "O":
            sum += row * 100 + col
print(sum)
