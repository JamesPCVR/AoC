def depth_first_search(area:list[list[int]], point:tuple[int,int,int], _from:int=None) -> list[tuple[int,int]]:
    """find the endpoints of increasing paths."""
    x, y, h = point
    if h == 9:
        return [(x, y)]

    reachable = []
    steps = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    avoid = [2, 3, 0, 1]

    x_lim = len(area[0]) - 1
    y_lim = len(area) - 1

    for i, step in enumerate(steps):
        if _from is not None and i == avoid[_from]:
            continue

        x_c = x + step[0]
        y_c = y + step[1]
        if x_c < 0 or x_c > x_lim:
            continue
        if y_c < 0 or y_c > y_lim:
            continue

        h_c = area[y_c][x_c]
        if h_c != h + 1:
            continue

        reachable.extend(depth_first_search(area, (x_c, y_c, h_c), i))

    return reachable

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    area = [[int(h) for h in line] for line in content]
    total_score = 0
    for y, line in enumerate(area):
        for x, space in enumerate(line):
            if space != 0:
                continue
            reachable = depth_first_search(area, (x, y, space))
            new = tuple(set(reachable))
            total_score += len(new)

    print(total_score)

if __name__ == "__main__":
    main()
    # 552
