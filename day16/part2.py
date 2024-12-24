from heapq import heappop, heappush
from typing import DefaultDict

with open("day16/example.txt", "r") as f:
    s = f.read().strip()

g = [list(r) for r in s.split("\n")]
n, m = len(g), len(g[0])
sx, sy = 0, 0
ex, ey = 0, 0

for i in range(n):
    for j in range(m):
        if g[i][j] == "S":
            sx, sy = i, j
            g[i][j] = "."
        if g[i][j] == "E":
            ex, ey = i, j
            g[i][j] = "."
cx, cy = sx, sy
sd = 0
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def adjs(cur):
    cx, cy, cd = cur
    yield 1000, (cx, cy, (cd - 1) % 4)
    yield 1000, (cx, cy, (cd + 1) % 4)
    dx, dy = dirs[cd]
    nx, ny = cx + dx, cy + dy
    if g[nx][ny] != "#":
        yield 1, (nx, ny, cd)


# dijkstra's
# x, y dir
start = (sx, sy, sd)
pq = []
p1 = None
heappush(pq, (0, start))
dists = DefaultDict(lambda: float("inf"))
from_ = DefaultDict(lambda: set())

while len(pq) > 0:
    dist, cur = heappop(pq)
    (cx, cy, cd) = cur
    if (cx, cy) == (ex, ey):
        if p1 is None:
            p1 = dist
            print(dist)
    for d, adj in adjs(cur):
        if dist + d < dists[adj]:
            dists[adj] = dist + d
            heappush(pq, (dists[adj], adj))
            from_[adj] = {cur}
        elif dist + d <= dists[adj]:
            from_[adj].add(cur)

for dr in range(4):
    print(dr, dists[ex, ey, dr])

stack = [(ex, ey, 1)]
gnodes = set(stack)
while len(stack) > 0:
    some = stack.pop(-1)
    for other in from_[some]:
        if other not in gnodes:
            gnodes.add(other)
            stack.append(other)
gnodes = set(x[:2] for x in gnodes)
print(len(gnodes))
print(
    "\n".join(
        "".join(g[i][j] if (i, j) not in gnodes else "O" for j in range(m))
        for i in range(n)
    )
)
