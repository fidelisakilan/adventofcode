file = open("day15/input.txt", "r").read().split("\n\n")

sections = file
warehouse_section = sections[0]
directions_section = sections[1]
warehouse_old = [line for line in warehouse_section.split("\n")]
steps = list(directions_section.replace("\n", ""))
transformation = {"#": "##", "O": "[]", ".": "..", "@": "@."}
DIRECTION_MAP = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


warehouse = []
for row in warehouse_old:
    warehouse.append(list("".join(transformation[tile] for tile in list(row))))
rows = len(warehouse)
cols = len(warehouse[0])


def print_matrix():
    for row in range(r):
        for col in range(c):
            print(warehouse[row][col], end="")
        print()


si, sj = 0, 0
for i in range(rows):
    for j in range(cols):
        if warehouse[i][j] == "@":
            si, sj = i, j

r, c = si, sj
for step in steps:
    d = DIRECTION_MAP[step]
    nr, nc = r + d[0], c + d[1]
    if warehouse[nr][nc] == "#":
        continue
    if warehouse[nr][nc] == ".":
        warehouse[r][c] = "."
        warehouse[nr][nc] = "@"
        r, c = nr, nc
        continue
    # Case 1: Push box(es) left/right
    if d[1] != 0:
        peek_c = nc

        # Peek until we see a blank space or a wall
        while warehouse[r][peek_c] != "." and warehouse[r][peek_c] != "#":
            peek_c += d[1]

        # Boxes are flush against a wall, no movement
        if warehouse[r][peek_c] == "#":
            continue

        # If we hit an open space, shift the previous cells 1 unit over
        shift_c = peek_c
        while shift_c != c - d[1]:
            warehouse[r][shift_c] = warehouse[r][shift_c - d[1]]
            shift_c -= d[1]
        warehouse[r][c] = "."
        c = nc
    # Case 2: Vertically shift boxes
    else:

        def get_shift_chain():
            queue = []
            queue.append((r, c))
            visited = {}
            visited[(nr, nc)] = warehouse[nr][nc]
            while queue:
                cur_r, cur_c = queue.pop(0)
                peek_r, peek_c = cur_r + d[0], cur_c + d[1]

                if warehouse[peek_r][peek_c] == "#":
                    return None
                if warehouse[peek_r][peek_c] == ".":
                    continue

                visited[(peek_r, peek_c)] = warehouse[peek_r][peek_c]
                if warehouse[peek_r][peek_c] == "[":
                    queue.append((peek_r, peek_c))
                    queue.append((peek_r, peek_c + 1))
                    visited[(peek_r, peek_c + 1)] = warehouse[peek_r][peek_c + 1]
                elif warehouse[peek_r][peek_c] == "]":
                    queue.append((peek_r, peek_c))
                    queue.append((peek_r, peek_c - 1))
                    visited[(peek_r, peek_c - 1)] = warehouse[peek_r][peek_c - 1]
            return visited

        pieces_to_shift = get_shift_chain()
        if pieces_to_shift:
            for pt, cell in pieces_to_shift.items():
                warehouse[pt[0]][pt[1]] = "."
            for pt, cell in pieces_to_shift.items():
                warehouse[pt[0] + d[0]][pt[1] + d[1]] = cell
            warehouse[r][c] = "."
            warehouse[nr][c] = "@"
            r, c = nr, nc


sum = 0
for row in range(rows):
    for col in range(cols):
        if warehouse[row][col] == "[":
            sum += row * 100 + col
print(sum)
