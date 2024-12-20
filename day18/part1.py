file = open("day18/example.txt", "r")

size = 6
bytes_size = 12
incoming_bytes = [map(int, line.strip().split(",")) for line in file.readlines()]
matrix = list(list("." for _ in range(0, size + 1)) for _ in range(0, size + 1))
rows = len(matrix)
cols = len(matrix[0])
start_pos, end_pos = (0, 0), (size, size)
directions = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]


for x, y in incoming_bytes:
    if bytes_size == 0:
        break
    matrix[y][x] = "#"
    bytes_size -= 1

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = "."


def findPath(curri, currj, path):
    if matrix[curri][currj] == "#":
        return
    if (curri, currj) == end_pos:
        return True

    elif matrix[curri][currj] == ".":
        for dir in directions:
            di, dj = dir
            ni, nj = (curri + di, currj + dj)
            if ni in range(0, size + 1) and nj in range(0, size + 1):
                pq.append((
                    (ni, nj),
                    path + [(curri, currj)],
                ))
    return


pq = [(start_pos, [])]
visited = []
while pq:
    (curri, currj), path = pq.pop(0)
    if ((curri, currj)) in visited:
        continue
    visited.append((curri, currj))
    result = findPath(curri, currj, path)
    if result is not None:
        break
print(matrix)
print(visited)
print(len(visited) - 1)
