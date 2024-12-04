file = open("input.txt", "r").readlines()

word_order = {0: "X", 1: "M", 2: "A", 3: "S"}
matrix = []
all_paths = set()

directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [-1, -1],
    [1, 1],
    [-1, 1],
    [1, -1],
]

for line in file:
    matrix.append(list(line.strip()))

n = len(matrix)
m = len(matrix[0])


def find_pattern(path, direction):
    previous_index = path[-1]
    current_index = (previous_index[0] + direction[0], previous_index[1] + direction[1])
    if not 0 <= current_index[0] < n or not 0 <= current_index[1] < m:
        return

    current_letter = matrix[current_index[0]][current_index[1]]
    if word_order[len(path)] == current_letter:
        if len(path) == 3:
            path.append(current_index)
            if tuple(path) not in all_paths:
                all_paths.add(tuple(path))
        else:
            find_pattern(path + [current_index], direction)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "X":
            for direction in directions:
                find_pattern([(i, j)], direction)

print(len(all_paths))
