file = open("example.txt", "r")

input_str = file.readline().strip()

disk_map = ""
disk_index = 0
checksum = 0
last_empty_index = 0

for index, letter in enumerate(list(input_str)):
    block = ""
    if index % 2 != 0:
        block = "".join(["." for _ in range(int(letter))])
    else:
        block = "".join([str(disk_index) for _ in range(int(letter))])
        disk_index += 1
    disk_map = disk_map + block
disk_length = len(disk_map)


def modify_disk(block):
    global disk_map, last_empty_index, checksum
    start = block[0]
    end = block[1]
    id = block[2]
    new_block = [id for _ in range(end - start + 1)]
    for i in range(start, end + 1):
        disk_map = disk_map[:i] + "." + disk_map[i + 1 :]

    for i in range(last_empty_index + 1, disk_length):
        if len(new_block) == 0:
            break
        if disk_map[i] == ".":
            last_empty_index = i
            disk_map = disk_map[:i] + new_block.pop() + disk_map[i + 1 :]
        checksum += int(disk_map[i]) * i

current = (disk_length - 1, disk_length - 1, disk_map[-1])
print(disk_map)
for i in reversed(range(disk_length)):
    if disk_map[i] == ".":
        continue
    if current[2] == disk_map[i]:
        current = (i, current[1], current[2])
        continue
    if last_empty_index > int(current[0]):
        break
    modify_disk(current)
    current = (i, i, disk_map[i])
print(disk_map)
print(checksum)
