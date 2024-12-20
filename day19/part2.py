file = open("day19/input.txt", "r").read()

stripes = file.split("\n\n")[0].split(", ")
patterns = file.split("\n\n")[1].strip().split("\n")

print(stripes)
print(patterns)

pattern_dict: dict[str, int] = {}


def find_path(stripes: list[str], pattern: str):
    if len(pattern) == 0:
        return 1

    if pattern in pattern_dict:
        return pattern_dict[pattern]

    combinations = 0
    for stripe in stripes:
        if pattern.startswith(stripe):
            combinations += find_path(stripes, pattern[len(stripe) :])
    pattern_dict[pattern] = combinations
    return combinations


count = 0
for pattern in patterns:
    count += find_path(stripes, pattern)

print(count)
