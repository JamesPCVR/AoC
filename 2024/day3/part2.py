import re

def do_mul(mul:str) -> int:
    nums = re.findall(r"\d{1,3}", mul)
    return int(nums[0]) * int(nums[1])

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read()

    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", content)
    enabled = True
    total = 0
    for mul in muls:
        if mul == "do()":
            enabled = True
        elif mul == "don't()":
            enabled = False
        else:
            if enabled:
                total += do_mul(mul)

    print(total)

if __name__ == "__main__":
    main()
    # 89823704
