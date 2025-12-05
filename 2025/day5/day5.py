FILENAME = "in.txt"

def is_fresh(ranges:list[tuple[int]], ingredient:int):
    """Check an ingredient exists in the valid ranges."""
    for br, tr in ranges:
        if br <= ingredient <= tr:
            return ingredient

    return 0

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blank_idx = lines.index("\n")
    ranges = [tuple(map(int, r.strip().split("-"))) for r in lines[:blank_idx]]
    ingredients = [int(i.strip()) for i in lines[blank_idx+1:]]

    fresh_count = 0
    for i in ingredients:
        fresh_count += bool(is_fresh(ranges, i))

    return fresh_count

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blank_idx = lines.index("\n")
    ranges = [tuple(map(int, r.strip().split("-"))) for r in lines[:blank_idx]]
    ranges.sort()

    valid_count = 0
    trt = 0
    for br, tr in ranges:
        if trt > br:
            br = trt
        if tr >= br:
            valid_count += tr - br + 1
        trt = max(trt, tr+1)

    return valid_count

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
