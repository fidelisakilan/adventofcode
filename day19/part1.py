file = open("day19/input.txt", "r").read()

stripes = file.split("\n\n")[0].split(", ")
patterns = file.split("\n\n")[1].strip().split("\n")

print(stripes)
print(patterns)

def find_path(stripes: list[str], pattern: str):
    if len(pattern) == 0:
        return True
    for stripe in stripes:
        if pattern.startswith(stripe):
            if find_path(stripes, pattern[len(stripe) :]):
                return True
    return False


count = 0
for pattern in patterns:
    if find_path(stripes, pattern):
        count += 1

print(count)
