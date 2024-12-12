file = open("day12/input.txt")

matrix = list(list(line.strip()) for line in file)
r = len(matrix)
c = len(matrix[0])

directions = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]

already_passed = set()
all_regions = []
props = []


def find_region(ci, cj, path, perimeter):
    path.append((ci, cj))
    already_passed.add((ci, cj))
    plant = matrix[ci][cj]
    perimeter += 4

    for dir in directions:
        next_index = (ci + dir[0], cj + dir[1])
        if next_index[0] not in range(r) or next_index[1] not in range(c):
            continue
        next_matrix = matrix[next_index[0]][next_index[1]]
        if next_matrix == plant:
            perimeter -= 1

    for dir in directions:
        next_index = (ci + dir[0], cj + dir[1])
        if next_index[0] not in range(r) or next_index[1] not in range(c):
            continue
        next_matrix = matrix[next_index[0]][next_index[1]]
        if next_matrix == plant and next_index not in path:
            perimeter = find_region(next_index[0], next_index[1], path, perimeter)
    return perimeter

for i in range(r):
    for j in range(c):
        path_taken = []
        if (i, j) not in already_passed:
            perimeter = find_region(i, j, path_taken, 0)
            props.append((len(path_taken), perimeter))
            all_regions.append(path_taken)
price = 0
for prop in props:
    price += prop[0] * prop[1]
print(price)
