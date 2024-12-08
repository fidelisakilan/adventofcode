import itertools

file = open("input.txt")

matrix = list(list(line.strip()) for line in file)
r = len(matrix)
c = len(matrix[0])
cmatrix = [["." for _ in range(c)] for _ in range(r)]

# Basically for any 2 numbers create a antinode in the matrix and then count the total numbers

antenna_dict = {}
for i in range(r):
    for j in range(c):
        pointer = matrix[i][j]
        if pointer.isalnum():
            antenna_dict[pointer] = antenna_dict.get(pointer, []) + [(i, j)]

count = 0
for key, value in antenna_dict.items():
    permutations = itertools.permutations(value, r=2)
    for pair in permutations:
        n1 = pair[0]
        n2 = pair[1]
        diffx = n1[0] - n2[0]
        diffy = n1[1] - n2[1]
        antinodes = (
            (n1[0] + diffx, n1[1] + diffy),
            (n2[0] - diffx, n2[1] - diffy),
        )
        print(pair, antinodes)
        for node in antinodes:
            if node[0] in range(r) and node[1] in range(c):
                cmatrix[node[0]][node[1]] = "#"
                count += 1

print("\n".join([" ".join(row) for row in cmatrix]))
print(sum(row.count("#") for row in cmatrix))