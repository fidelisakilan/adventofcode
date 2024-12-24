def p1():
    def mix(value, number):
        xor = value ^ number
        return xor

    def prune(number):
        return number % 16777216

    def calculate_next_secret(number):
        number = prune(mix(number * 64, number))
        number = prune(mix(number // 32, number))
        number = prune(mix(number * 2048, number))
        return number

    sum = 0
    for i in open("input/22.txt").readlines():
        secret_number = int(i)
        for _ in range(2000):
            secret_number = calculate_next_secret(secret_number)
        sum += secret_number
    print("p1: ", sum)


def p2():
    def mix(value, number):
        xor = value ^ number
        return xor

    def prune(number):
        return number % 16777216

    def calculate_next_secret(number):
        number = prune(mix(number * 64, number))
        number = prune(mix(number // 32, number))
        number = prune(mix(number * 2048, number))
        return number

    sums = {}
    for i in open("input/22.txt").readlines():
        secret = int(i)
        changes = []
        out = {}
        for _ in range(2000):
            old_price = secret % 10
            secret = calculate_next_secret(secret)
            new_price = secret % 10
            price_change = new_price - old_price
            changes.append(price_change)
            if len(changes) == 4:
                sequence_key = tuple(changes)
                if sequence_key not in out:
                    out[sequence_key] = new_price
                changes.pop(0)
        for k, v in out.items():
            sums[k] = sums.get(k, 0) + v
    print("p2: ", max(sums.values()))

p1()
p2()
