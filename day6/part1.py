file = open("input.txt", "r").readlines()

matrix = []
distinct_locations = set()
si, sj = 0, 0
cdir = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

for line in file:
    matrix.append(list(line.strip()))

rows = len(matrix)
columns = len(matrix[0])

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == "^":
            si, sj = (i, j)

cd = 0
i, j = si, sj
while i in range(rows) and j in range(columns):
    ni, nj = i + cdir[cd][0], j + cdir[cd][1]
    if matrix[ni][nj] == "#":
        cd = (cd + 1) % 4
    else:
        i, j = ni, nj
        distinct_locations.add((i, j))
print(len(distinct_locations))
