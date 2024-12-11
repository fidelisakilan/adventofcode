with open("day9/input.txt") as f:
    file = f.read().strip()
disk = []

free_space = []

for i in range(len(file)):
    file_id = ""
    if i % 2 == 0:
        file_id = i // 2
    else:
        file_id = "."
        if int(file[i]) != 0:
            free_space.append([len(disk), len(disk) + int(file[i]) - 1])
    disk.extend([file_id] * int(file[i]))
free_space.reverse()

free_index = free_space.pop()

for i in reversed(range(len(disk))):
    if disk[i] == ".":
        continue
    # print(free_index, i, "".join(str(x) for x in disk))
    if free_index[0] < i:
        disk[free_index[0]] = disk[i]
        disk[i] = "."
        free_index[0] += 1

    if free_index[0] > free_index[1]:
        if len(free_space) == 0:
            break
        free_index = free_space.pop()

checksum = 0
for i,j in enumerate(disk):
    if j != ".":
        checksum += i*j
print(checksum)
