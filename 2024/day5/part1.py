def check_rules(rules:list[list[int]], pages:list[int]) -> int:
    """returns the middle page number if rules not violated"""
    for rule in rules:
        try:
            pos = pages.index(rule[0])
            for page_before in pages[:pos]:
                if page_before == rule[1]:
                    print(f"{pages} violates {rule[0]}|{rule[1]}")
                    return 0
        except ValueError:
            continue
    return pages[len(pages)//2]

def main():
    with open("inrules.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")
    rules = [[int(r) for r in line.split("|")] for line in content]
    rules.sort()

    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")
    manuals = [[int(p) for p in line.split(",")] for line in content]

    middle_total = 0
    for pages in manuals:
        middle_total += check_rules(rules, pages)

    print(middle_total)

if __name__ == "__main__":
    main()
    # 4185
