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

def perimeter(region:set[tuple[int,int]]) -> int:
    """find the perimeter of a region."""
    steps = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    perim = 0
    for x, y in region:
        for x_step, y_step in steps:
            x_c = x + x_step
            y_c = y + y_step
            if (x_c, y_c) in region:
                continue
            perim += 1
    return perim

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
                p = perimeter(region)
                total_price += a * p

    print(total_price)

if __name__ == "__main__":
    main()
    # 1522850
