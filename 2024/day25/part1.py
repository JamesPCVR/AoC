from itertools import product

def to_heights(_map:list[str]) -> tuple[int]:
    """convert key or lock map to height map"""
    heights = [-1, -1, -1, -1, -1]
    for line in _map:
        for i, char in enumerate(line):
            if char == "#":
                heights[i] += 1
    return tuple(heights)

def does_fit(key:tuple[int], lock:tuple[int]) -> bool:
    """check if key can fit in the lock"""
    diff = [k + l for k, l in zip(key, lock)]
    return all(map(lambda x: x<=5, diff))

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        keys_locks = f.read().split("\n\n")

    keys = set()
    locks = set()
    for key_lock in keys_locks:
        lines = key_lock.split("\n")
        heights = to_heights(lines)
        if lines[0] == "#####":
            keys.add(heights)
        else:
            locks.add(heights)

    can_fit = 0
    for key, lock in product(keys, locks):
        if does_fit(key, lock):
            can_fit += 1

    print(can_fit)

if __name__ == "__main__":
    main()
    # 10954 too high
    # 3365
