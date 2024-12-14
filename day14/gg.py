from collections import defaultdict


file = open("day14/input.txt", "r")
r = 103
c = 101

iterations = 100
robots = {}
matrix = defaultdict(set)


def print_matrix():
    print()
    for row in range(r):
        for col in range(c):
            if (col, row) in matrix:
                print(len(matrix[(col, row)]), end=" ")
            else:
                print(0, end=" ")
        print()


object_index = 0
for line in file.readlines():
    st = line.split(" ")
    p_str, v_str = st[0], st[1]
    px = int(p_str.replace("p=", "").split(",")[0])
    py = int(p_str.replace("p=", "").split(",")[1])
    vx = int(v_str.replace("v=", "").split(",")[0])
    vy = int(v_str.replace("v=", "").split(",")[1])
    robots[object_index] = {"p": (px, py), "v": (vx, vy)}
    object_index += 1


for key, value in robots.items():
    p = value["p"]
    matrix[p].add(key)

print_matrix()
for itr in range(iterations):
    new_matrix = defaultdict(set)
    for i in range(r):
        for j in range(c):
            robots_in_tile = matrix[(j, i)]
            skipped = 0
            while (len(robots_in_tile) - skipped) > 0:
                robot_index = robots_in_tile.pop()
                velocity = robots[robot_index]["v"]
                nx, ny = (j + velocity[0] + c) % c, (i + velocity[1] + r) % r
                new_matrix[(nx, ny)].add(robot_index)
        matrix = new_matrix

print_matrix()
midx, midy = c // 2, r // 2
count = 0
quad1, quad2, quad3, quad4 = 0, 0, 0, 0
for i in range(r):
    for j in range(c):
        if i == midy or j == midx:
            continue
        if i < midy and j < midx:
            quad1 += len(matrix[(j, i)])
        elif i < midy and j > midx:
            quad2 += len(matrix[(j, i)])
        elif i > midy and j < midx:
            quad3 += len(matrix[(j, i)])
        elif i > midy and j > midx:
            quad4 += len(matrix[(j, i)])
print(quad1 * quad2 * quad3 * quad4)
