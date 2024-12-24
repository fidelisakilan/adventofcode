import heapq

with open("day20/example.txt", "r") as f:
    s = f.read().strip()

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
g = [list(r) for r in s.split("\n")]
n, m = len(g), len(g[0])
sx, sy = 0, 0
ex, ey = 0, 0
pq = []

for i in range(n):
    for j in range(m):
        if g[i][j] == "S":
            sx, sy = i, j
        if g[i][j] == "E":
            ex, ey = i, j
print(sx, sy, ex, ey)


def findPath(matrix, cost, cx, cy):
    if matrix[cx][cy] == "#":
        return
    if (cx, cy) == (ex, ey):
        return cost

    elif matrix[cx][cy] in ".S":
        for dir in dirs:
            dx, dy = dir
            heapq.heappush(pq, (cost + 1, cx + dx, cy + dy))
    return


heapq.heappush(pq, (0, sx, sy))
visited = set()
while pq:
    cost, cx, cy = heapq.heappop(pq)
    print(cx, cy)
    if (cx, cy) in visited:
        continue
    visited.add((cx, cy))
    result = findPath(g, cost, cx, cy)
    if result is not None:
        print(result)
        break
