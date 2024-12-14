file = open("day14/input.txt", "r")
lines = file.readlines()
total = len(lines)

print(total)

for steps in range(1, 100000):
    seen = set()
    for line in lines:
        st = line.split(" ")
        p_str, v_str = st[0], st[1]
        px = int(p_str.replace("p=", "").split(",")[0])
        py = int(p_str.replace("p=", "").split(",")[1])
        vx = int(v_str.replace("v=", "").split(",")[0])
        vy = int(v_str.replace("v=", "").split(",")[1])
        nx = (px + steps * vx) % 101
        ny = (py + steps * vy) % 103
        seen.add((nx,ny))
    if len(seen) == total:
        print(steps)
        break
