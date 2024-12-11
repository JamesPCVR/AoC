import re

def do_mul(mul:str) -> int:
    nums = re.findall(r"\d{1,3}", mul)
    return int(nums[0]) * int(nums[1])

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read()

    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", content)
    res = map(do_mul, muls)

    print(sum(res))

if __name__ == "__main__":
    main()
    # 167090022
