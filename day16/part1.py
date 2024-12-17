import heapq

file = open("day16/input.txt", "r")
matrix = list(list(line.strip()) for line in file)
rows = len(matrix)
cols = len(matrix[0])
start_pos, end_pos = (0, 0), (0, 0)
pq = []

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "S":
            start_pos = (i, j)
        elif matrix[i][j] == "E":
            end_pos = (i, j)


def findPath(curri, currj, currdir, points):
    if matrix[curri][currj] == "#":
        return
    if (curri, currj) == end_pos:
        return points

    elif matrix[curri][currj] in ".S":
        directions = [
            (currdir[0], currdir[1]),
            (currdir[1], -currdir[0]),
            (-currdir[1], currdir[0]),
        ]
        for dir in directions:
            di, dj = dir
            heapq.heappush(
                pq,
                (
                    points + (1 if currdir == dir else 1001),
                    (curri + di, currj + dj),
                    dir,
                ),
            )
    return


heapq.heappush(pq, (0, start_pos, (0, 1)))
visited = set()
while pq:
    points, (curri, currj), currdir = heapq.heappop(pq)
    if ((curri, currj), currdir) in visited:
        continue
    visited.add(((curri, currj), currdir))
    result = findPath(curri, currj, currdir, points)
    if result is not None:
        print(result)
        break
