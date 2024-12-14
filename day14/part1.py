file = open("day14/input.txt", "r")


quad1, quad2, quad3, quad4 = 0, 0, 0, 0
for line in file.readlines():
    st = line.split(" ")
    p_str, v_str = st[0], st[1]
    px = int(p_str.replace("p=", "").split(",")[0])
    py = int(p_str.replace("p=", "").split(",")[1])
    vx = int(v_str.replace("v=", "").split(",")[0])
    vy = int(v_str.replace("v=", "").split(",")[1])
    nx = (px + 100 * vx) % 101
    ny = (py + 100 * vy) % 103
    if nx < 50 and ny < 51:
        quad1 += 1
    elif nx > 50 and ny < 51:
        quad2 += 1
    elif nx < 50 and ny > 51:
        quad3 += 1
    elif nx > 50 and ny > 51:
        quad4 += 1

print(quad1 * quad2 * quad3 * quad4)
