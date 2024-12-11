file = open("input.txt")

matrix = list(list(line.strip()) for line in file)
r = len(matrix)
c = len(matrix[0])

trails = []

directions = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]


def check_trailhead_p1(start, i, j):
    print("check_trailhead", start, i, j)
    number = int(matrix[i][j])
    if number == 9:
        if (start, (i, j)) not in trails:
            trails.append((start, (i, j)))
        return
    for dir in directions:
        nextR, nextC = i + dir[0], j + dir[1]
        if nextR not in range(r) or nextC not in range(c):
            continue
        if int(matrix[nextR][nextC]) - number == 1:
            check_trailhead_p1(start, nextR, nextC)

def check_trailhead_p2(start, i, j):
    print("check_trailhead", start, i, j)
    number = int(matrix[i][j])
    if number == 9:
        trails.append((start, (i, j)))
        return
    for dir in directions:
        nextR, nextC = i + dir[0], j + dir[1]
        if nextR not in range(r) or nextC not in range(c):
            continue
        if int(matrix[nextR][nextC]) - number == 1:
            check_trailhead_p2(start, nextR, nextC)


for i in range(r):
    for j in range(c):
        number = int(matrix[i][j])
        if number == 0:
            check_trailhead_p2((i, j), i, j)

print(len(trails))
