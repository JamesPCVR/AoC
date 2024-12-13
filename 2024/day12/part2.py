def depth_first_search(farm:list[list[str]], start:tuple[int,int], item:str, visited:set[tuple[int,int]]=None) -> set[tuple[int,int]]:
    """search for all neighbouring `item`s and return their coordinates."""
    steps = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    x_lim = len(farm[0]) - 1
    y_lim = len(farm) - 1

    x, y = start
    if visited is None:
        visited = set()
    visited.add(start)

    for x_step, y_step in steps:
        x_c = x + x_step
        y_c = y + y_step
        if x_c < 0 or x_c > x_lim:
            continue
        if y_c < 0 or y_c > y_lim:
            continue
        if (x_c, y_c) in visited:
            continue
        if farm[y_c][x_c] != item:
            continue

        visited = visited.union(
            depth_first_search(farm, (x_c, y_c), item, visited)
        )

    return visited

def area(region:set[tuple[int,int]]) -> int:
    """find the area of a region"""
    return len(region)

def scan_side(region:set[tuple[int,int]], start:tuple[int,int], direction:tuple[int,int], side:tuple[int,int]) -> set[tuple[int,int]|str]:
    """scan for a side of a region"""
    side_points = set()
    direc = {
        (1, 0): "right",
        (0, -1): "up",
        (-1, 0): "left",
        (0, 1): "down",
    }
    side_points.add(direc[side])
    side_points.add(start)
    x, y = start
    count = 1
    while True:
        x_t = x + direction[0]*count
        y_t = y + direction[1]*count
        if (x_t, y_t) in region:
            break
        x_c = x_t + side[0]
        y_c = y_t + side[1]
        if (x_c, y_c) not in region:
            break
        side_points.add((x_t, y_t))
        count += 1
    count = 1
    while True:
        x_t = x - direction[0]*count
        y_t = y - direction[1]*count
        if (x_t, y_t) in region:
            break
        x_c = x_t + side[0]
        y_c = y_t + side[1]
        if (x_c, y_c) not in region:
            break
        side_points.add((x_t, y_t))
        count += 1
    return side_points

def sides(region:set[tuple[int,int]]) -> int:
    """find the number of sides of a region."""
    steps = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    all_sides = set()

    for x, y in region:
        for x_step, y_step in steps:
            x_c = x + x_step
            y_c = y + y_step
            if (x_c, y_c) in region:
                continue

            found_side = frozenset(
                scan_side(
                    region,
                    (x_c, y_c),
                    (y_step, x_step),
                    (-x_step, -y_step)
                )
            )
            if found_side in all_sides:
                continue

            all_sides.add(found_side)

    return len(all_sides)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        farm = [list(line) for line in f.read().split("\n")]

    unvisited = set(
        (x, y) for y, line in enumerate(farm) for x in range(len(line))
    )

    total_price = 0
    for y, line in enumerate(farm):
        for x, plot in enumerate(line):
            if (x, y) in unvisited:
                region = depth_first_search(farm, (x, y), plot)
                unvisited = unvisited.difference(region)
                a = area(region)
                s = sides(region)
                total_price += a * s

    print(total_price)

if __name__ == "__main__":
    main()
    # 953738
