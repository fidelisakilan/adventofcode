with open("day9/example.txt") as f:
    file = f.read().strip()
disk = []
disk_space = []
free_space = []

for i in range(len(file)):
    file_id = ""
    if i % 2 == 0:
        file_id = i // 2
        disk_space.append([len(disk), len(disk) + int(file[i]) - 1, file_id])
    else:
        file_id = "."
        if int(file[i]) != 0:
            free_space.append([len(disk), len(disk) + int(file[i]) - 1])
    disk.extend([file_id] * int(file[i]))

file_count = len(disk_space)


for i in reversed(range(file_count)):
    current_file = disk_space[i]
    required_size = current_file[1] - current_file[0] + 1
    for j in free_space:
        available_size = j[1] - j[0] + 1
        if j[0] < current_file[0] and required_size <= available_size:
            disk_space[i] = [j[0], j[0] + required_size - 1, current_file[2]]
            free_space.remove(j)
            if required_size < available_size:
                free_space.append([j[0] + required_size - 1, j[1]])
            free_space.append([current_file[0], current_file[1]])
            break
    # print("DISK: ", disk_space)
    # print("FREE: ", free_space)

checksum = 0
for file in disk_space:
    checksum += sum(range(file[0], file[1] + 1)) * file[2]

print(checksum)
