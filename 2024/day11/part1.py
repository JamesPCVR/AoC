def digits(num:int) -> int:
    """returns number of digits in int."""
    return len(f"{num}")

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        start = [int(n) for n in f.read().split(" ")]

    nums2 = {}
    for n in start:
        nums2[n] = 1

    for _ in range(25):
        nums1 = nums2.copy()
        del nums2
        nums2 = {}
        for n, c in nums1.items():
            if n == 0:
                # 0, becomes 1
                if 1 in nums2:
                    nums2[1] += c
                else:
                    nums2[1] = c
            elif (d := digits(n)) % 2 == 0:
                # even digits, split it
                s = str(n)
                p = d // 2
                n1 = int(s[:p])
                n2 = int(s[p:])

                if n1 in nums2:
                    nums2[n1] += c
                else:
                    nums2[n1] = c
                if n2 in nums2:
                    nums2[n2] += c
                else:
                    nums2[n2] = c
            else:
                # odd digits, multiply it
                k = n * 2024
                if k in nums2:
                    nums2[k] += c
                else:
                    nums2[k] = c

    count = 0
    for c in nums2.values():
        count += c

    print(count)

if __name__ == "__main__":
    main()
    # 199982
