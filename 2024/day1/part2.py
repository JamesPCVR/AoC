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

    similarity = 0
    for num in left:
        similarity += int(num) * right.count(num)

    print(similarity)

if __name__ == "__main__":
    main()
