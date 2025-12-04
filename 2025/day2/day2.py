FILENAME = "test.txt"

def find_doubled(bottom:int, top:int): # pylint: disable= C0116
    doubles = []
    trim = sum(divmod(len(str(bottom)), 2))
    num = 10 ** (trim -1)
    while True:
        snum = str(num) * 2
        num += 1

        if int(snum) < bottom:
            continue
        if int(snum) > top:
            break

        doubles.append(int(snum))

    return doubles

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

    count = 0
    for range_ in ranges:
        doubles = find_doubled(int(range_[0]), int(range_[1]))
        count += sum(doubles)

    return count

def all_same(string:str):
    """string contains only one character."""
    return string == len(string) * string[0] # this is faster apparently
    # return all(c == string[0] for c in string)

def is_repeating(num:int): # pylint: disable= C0116
    snum = str(num)
    length = len(snum)
    for n in range(1, length//2 + 1):
        # cannot be divided into n parts
        if length % n != 0:
            continue

        repeating = all(all_same(snum[i::n]) for i in range(n))
        if repeating:
            return True

    return False

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

    count = 0
    for range_ in ranges:
        start = range_[0]
        end = range_[1] + 1
        for num in range(start, end):
            count += num * is_repeating(num)

    return count

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")