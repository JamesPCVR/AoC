def verify_maths(target:int, nums:list[int]) -> bool:
    """checks if target can be made with numbers using + and *"""
    num_ops = len(nums) - 1
    for ops in range(2**num_ops):
        n1 = nums[0]
        for op in range(num_ops):
            n2 = nums[op+1]
            bit = (ops>>op) & 0x1
            if bit:
                t = n1 * n2
            else:
                t = n1 + n2
            n1 = t
        if n1 == target:
            return True
    return False

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    total = 0
    for line in content:
        key, val = line.split(": ")
        nums = tuple(map(int, val.split(" ")))
        target = int(key)
        if verify_maths(target, nums):
            total += target

    print(total)

if __name__ == "__main__":
    main()
    # 7885693428160 too low
    # OH MY GOD, the problem is a single duplicate key. AAAAH!
    # I spent far too long trying to figure that one out.
    # 7885693428401
