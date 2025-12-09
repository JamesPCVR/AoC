from itertools import combinations

FILENAME = "in.txt"

def area(p1:tuple[int,int], p2:tuple[int,int]):
    """The area of a rectangle cornered by the points."""
    dx = abs(p1[0] - p2[0]) + 1
    dy = abs(p1[1] - p2[1]) + 1
    return dx * dy

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        coords:list[tuple[int,int]] = [
            tuple(map(int, line.split(",", maxsplit=1)))
            for line in f.readlines()
        ]

    return max(area(*points) for points in combinations(coords, 2))

def is_point_within(coords:set[tuple[int,int]], p1:tuple[int,int], p2:tuple[int,int]):
    """Check if another point exists within the bounding box."""
    # new point 1 always lower-left and 2 always upper-right
    new_p1 = (min(p1[0], p2[0]), min(p1[1], p2[1]))
    new_p2 = (max(p1[0], p2[0]), max(p1[1], p2[1]))
    for x, y in coords:
        # a point on the border is still "outside"
        # it does not affect the ability to draw a rectangle
        if (new_p1[0] < x < new_p2[0]
            and new_p1[1] < y < new_p2[1]):
            return True

    return False

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        coords:list[tuple[int,int]] = [
            tuple(map(int, line.split(",", maxsplit=1)))
            for line in f.readlines()
        ]

    # traverse the loop, marking all invalid coordinates
    edge_coords = set()
    for p1, p2 in zip(coords, coords[1:]+coords[0:1]):
        p1x, p1y = p1
        p2x, p2y = p2
        if p1x == p2x:
            # iterate over y, p1y must be smaller
            if p2y < p1y:
                p1y, p2y = p2y, p1y
            edge_coords.update((p1x, y) for y in range(p1y, p2y+1))
        else:
            # iterate over x, p1x must be smaller
            if p2x < p1x:
                p1x, p2x = p2x, p1x
            edge_coords.update((x, p1y) for x in range(p1x, p2x+1))

    max_area = 0
    for p1, p2 in combinations(coords, 2):
        if not is_point_within(edge_coords, p1, p2):
            max_area = max(max_area, area(p1, p2))

    return max_area

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
