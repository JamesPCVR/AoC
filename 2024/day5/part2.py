def find_rules(rules:list[list[int]], pages:list[int]) -> int:
    """returns the middle page number if rules not violated"""
    corrected = True
    first = True
    while corrected is True:
        for rule in rules:
            try:
                pos = pages.index(rule[0])
                corrected = check_rule(rule, pages, pos)
                if corrected:
                    break
            except ValueError:
                continue
        if not corrected and first:
            return 0
        first = False
    return pages[len(pages)//2]

def check_rule(rule:list[int], pages:list[int], pos:int) -> None:
    """return true if pages had to be corrected"""
    for page_before in pages[:pos]:
        if page_before == rule[1]:
            correct_rule(rule, pages)
            return True
    return False

def correct_rule(rule:list[int], pages:list[int]) -> list[int]:
    """put violating rule immediately before its element"""
    i1 = pages.index(rule[0])
    i2 = pages.index(rule[1])
    val = pages.pop(i1)
    pages.insert(i2, val)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        rules, manuals = f.read().split("\n\n")
    rules = [[int(r) for r in line.split("|")] for line in rules.split("\n")]
    rules.sort()
    manuals = [[int(p) for p in line.split(",")] for line in manuals.split("\n")]

    middle_total = 0
    for pages in manuals:
        middle_total += find_rules(rules, pages)

    print(middle_total)

if __name__ == "__main__":
    main()
    # 4480
