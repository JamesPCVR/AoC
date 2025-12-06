from itertools import groupby

FILENAME = "test.txt"

def product(nums:list[int]):
    product = 1
    for n in nums:
        product *= n
    return product

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total = 0
    for problem in zip(*[line.split() for line in lines]):
        nums = list(map(int, problem[:-1]))
        op = problem[-1]

        if op == "+":
            total += sum(nums)
        else:
            total += product(nums)

    return total

def int_or_zero(string:str):
    """convert to int, 0 if blank or empty."""
    try:
        return int(string)
    except ValueError:
        return 0

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    numbers = [
        int_or_zero("".join(column))
        for column in zip(*lines[:-1])
    ]

    operations = lines[-1].split()

    groups = [
        tuple(group)
        for key, group in groupby(numbers, key=lambda x: x != 0)
        if key
    ]

    total = 0
    for nums, op in zip(groups, operations):
        if op == "+":
            total += sum(nums)
        else:
            total += product(nums)

    return total

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
