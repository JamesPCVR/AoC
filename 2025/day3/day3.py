FILENAME = "test.txt"

def highest_digit(bank:str): # pylint: disable= C0116
    return int(max(set(bank)))

def highest_joltage(bank:str): # pylint: disable= C0116
    # highest battery excluding the last
    high = highest_digit(bank[:-1])
    high_idx = bank.index(str(high))

    # next highest digit after that
    low = highest_digit(bank[high_idx+1:])

    return high*10 + low

def highest_joltage_ranged(bank:str, batteries:int): # pylint: disable= C0116
    total_joltage = 0
    index = 0
    for i in range(batteries):
        if i == batteries-1:
            segment = bank[index:]
        else:
            segment = bank[index:i-batteries+1]

        jolts = highest_digit(segment)
        index += segment.index(str(jolts)) + 1
        total_joltage *= 10
        total_joltage += jolts

    return total_joltage

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        total = sum((highest_joltage(line.strip()) for line in f.readlines()))

    return total

def part_2(): # pylint: disbale= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        total = sum((highest_joltage_ranged(line.strip(), 12)) for line in f.readlines())

    return total

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")