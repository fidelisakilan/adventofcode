file = open("input.txt", "r").readlines()

matrix = []
dir = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
si, sj = 0, 0

matrix = list(list(line.strip()) for line in file)
rows = len(matrix)
columns = len(matrix[0])

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == "^":
            si, sj = (i, j)
            break

count = 0
for i in range(rows):
    print(i)
    for j in range(columns):
        if matrix[i][j] == "#" or matrix[i][j] == "^":
            continue
        matrix[i][j] = "#"
        seen = set()
        cd = 0
        ci, cj = si, sj
        while ci in range(rows) and cj in range(columns) and (ci, cj, cd) not in seen:
            seen.add((ci, cj, cd))
            cdir = dir[cd]
            ni, nj = ci + cdir[0], cj + cdir[1]
            if ni in range(rows) and nj in range(columns) and matrix[ni][nj] == "#":
                cd = (cd + 1) % 4
            else:
                ci, cj = ni, nj
        if (ci, cj, cd) in seen:
            count += 1
        matrix[i][j] = "."
print(count)
