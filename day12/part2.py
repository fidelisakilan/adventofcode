from collections import defaultdict

file = open("day12/input.txt")

matrix = list(list(line.strip()) for line in file)
r = len(matrix)
c = len(matrix[0])

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# traversed will contain each point with then corresponding region
# k = point(x, y), v = region_index
traversed = {}


def find_region(i, j, label, nxt):
    if i in range(r) and j in range(c):
        if (i, j) in traversed:
            return
        if matrix[i][j] == label:
            traversed[i, j] = nxt
            for di, dj in directions:
                find_region(i + di, j + dj, label, nxt)


nxt = 0
for i in range(r):
    for j in range(c):
        if (i, j) not in traversed:
            find_region(i, j, matrix[i][j], nxt)
            nxt += 1

# reverse of traversed which will have set of points which belong to a region
# k = region_index, v = list of points
regions = defaultdict(set)

for k, v in traversed.items():
    regions[v].add(k)

part1 = 0
part2 = 0
for region, nodes in regions.items():
    area = len(nodes)
    # contain all nodes which are in the outer part of the region along with the outer index
    per = []
    for node in nodes:
        for di, dj in directions:
            ni, nj = node[0] + di, node[1] + dj
            if ni not in range(r) or nj not in range(c) or (ni, nj) not in nodes:
                per.append((node, (di, dj)))
    per = set(per)
    # contains all the unique nodes in the outer part of the region facing a direction
    sides = set()
    for p1, p2 in per:
        keep = True
        for dx, dy in [(1, 0), (0, 1)]:
            p1n = (p1[0] + dx, p1[1] + dy)
            p2n = (p2[0], p2[1])
            if (p1n, p2n) in per:
                keep = False
        if keep:
            sides.add((p1, (p1[0] + p2[0], p1[1] + p2[1])))
    part1 += area * len(per)
    part2 += area * len(sides)
print(part1, part2)
