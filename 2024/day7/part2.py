def ternary(n):
    # https://stackoverflow.com/questions/34559663
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def verify_maths(target:int, nums:list[int]) -> bool:
    """checks if target can be made with numbers using +, *, and ||"""
    num_ops = len(nums) - 1
    for ops in range(3**num_ops):
        n1 = nums[0]
        ops_t = f"{ternary(ops):0>{num_ops}s}"
        for i, op in enumerate(ops_t):
            n2 = nums[i+1]
            if op == "2":
                t = int(str(n1) + str(n2))
            elif op == "1":
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
    # 348360680516005
