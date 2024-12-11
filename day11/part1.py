with open("day11/example.txt") as f:
    stones = [int(x) for x in f.read().strip(" ").split()]


for i in range(25):
    new_stones = stones[:]
    index_add = 0
    for index, stone in enumerate(stones):
        if stone == 0:
            new_stones[index_add] = 1
            index_add += 1
        elif len(str(stone)) % 2 == 0:
            half_length = int(len(str(stone)) / 2)
            first_half = int(str(stone)[:half_length])
            second_half = int(str(stone)[half_length:])
            new_stones = (
                new_stones[:index_add]
                + [first_half, second_half]
                + new_stones[index_add + 1 :]
            )
            index_add += 2
        else:
            new_stones[index_add] = stone * 2024
            index_add += 1
    # print(i + 1, stones, new_stones)
    stones = new_stones
