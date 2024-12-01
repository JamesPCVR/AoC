import re

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    nums = re.split("\s+", content)

    left = []
    right = []
    for i, num in enumerate(nums):
        if num == "":
            continue
        if i%2 == 0:
            left.append(int(num))
        else:
            right.append(int(num))
    left.sort()
    right.sort()
    
    delta_total = 0
    for l, r in zip(left, right):
        delta_total += abs(l-r)
    
    print(delta_total)

if __name__ == "__main__":
    main()