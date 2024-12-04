from collections import Counter

file = open("input.txt", "r").readlines()

matrix = []
all_paths = set()

directions = [
    [[-1, -1], [1, 1]],
    [[-1, 1], [1, -1]],
]

for line in file:
    matrix.append(list(line.strip()))

n = len(matrix)
m = len(matrix[0])


def find_pattern(center_index):
    path = []
    for direction in directions:
        traversed_sides = []
        count = Counter()

        for side in direction:
            new_index = (center_index[0] + side[0], center_index[1] + side[1])
            if not (0 <= new_index[0] < n and 0 <= new_index[1] < m):
                return
            next_letter = matrix[new_index[0]][new_index[1]]
            if not (next_letter == "M" or next_letter == "S"):
                return
            count.update(next_letter)
            traversed_sides.append(new_index)

        if not (count["M"] == 1 and count["S"] == 1):
            return

        path.extend(traversed_sides)

    if tuple(path) not in all_paths:
        all_paths.add(tuple(path))


for i in range(n):
    for j in range(m):
        if matrix[i][j] == "A":
            find_pattern((i, j))

print(len(all_paths))
