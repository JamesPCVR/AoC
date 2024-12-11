def list_diff(_list:list[int]) -> list[int]:
    return [_list[i+1]-_list[i] for i in range(len(_list)-1)]

def is_safe(report:list[int]) -> bool:
    delta_set = set(list_diff(report))

    if delta_set.issubset({1, 2, 3}):
        return True
    if delta_set.issubset({-3, -2, -1}):
        return True

    return False

def is_safe_dampened(report:list[int]) -> bool:
    for i in range(len(report)):
        report_pop = report[:i] + report[i+1:]
        if is_safe(report_pop):
            return True
    return False

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    reports = [[int(num) for num in line.split(" ")] for line in lines]

    safe = sum(map(lambda rep: (is_safe(rep) or is_safe_dampened(rep)), reports))
    print(safe)

if __name__ == "__main__":
    main()
    # 612
