import typing
import fractions

def find_pairs(singles:list, reverse:bool) -> typing.Generator[tuple[tuple], None, None]:
    """Generate of the pairs of elements in a list"""
    for i, a in enumerate(singles):
        for b in singles[(i+1):]:
            yield a, b
            if reverse:
                yield b, a

def find_grid_on_line(coord_a:tuple[int], coord_b:tuple[int], list_:list[list[str]]) -> typing.Generator[tuple[int], None, None]:
    """generate all grid points of a line through two points"""
    dx = coord_b[0] - coord_a[0]
    dy = coord_b[1] - coord_a[1]
    dy_dx = fractions.Fraction(dy, dx)
    dy, dx = dy_dx.as_integer_ratio()
    tx = coord_a[0]
    ty = coord_a[1]
    while is_in_bounds(tx, ty, list_):
        yield tx, ty
        tx += dx
        ty += dy
    tx = coord_a[0] - dx
    ty = coord_a[1] - dy
    while is_in_bounds(tx, ty, list_):
        yield tx, ty
        tx -= dx
        ty -= dy

def is_in_bounds(x:int, y:int, list_:list[list[str]]) -> bool:
    """Check index is within list bounds"""
    x_lim = len(list_[0]) - 1
    y_lim = len(list_) - 1
    if x < 0 or x > x_lim:
        return False
    if y < 0 or y > y_lim:
        return False
    return True

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    antennas:dict[str,list] = {}
    for y, line in enumerate(content):
        for x, ant in enumerate(line):
            if ant == ".":
                continue
            if ant in antennas:
                antennas[ant].append((x, y))
            else:
                antennas[ant] = [(x, y)]

    antinodes = [["." for _ in line] for line in content]
    count = 0
    for freq in antennas.values():
        for a, b in find_pairs(freq, False):
            for x, y in find_grid_on_line(a, b, antinodes):
                if antinodes[y][x] != "#":
                    antinodes[y][x] = "#"
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
