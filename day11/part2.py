from collections import defaultdict

with open("day11/input.txt") as f:
    stones = defaultdict(int)
    for x in f.read().strip(" ").split():
        stones[int(x)] = 1

for i in range(75):
    cache = {}
    for key, value in stones.items():
        if key == 0:
            cache[1] = cache.get(1, 0) + value
        elif len(str(key)) % 2 == 0:
            half_length = int(len(str(key)) / 2)
            first_half = int(str(key)[:half_length])
            second_half = int(str(key)[half_length:])
            cache[first_half] = cache.get(first_half, 0) + value
            cache[second_half] = cache.get(second_half, 0) + value
        else:
            cache[key * 2024] = cache.get(key * 2024, 0) + value
    stones = cache
    print(stones)
stone_count = 0
for k, v in stones.items():
    stone_count += v

print(stone_count)
