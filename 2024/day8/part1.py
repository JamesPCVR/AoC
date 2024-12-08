import typing

def find_pairs(singles:list, reverse:bool) -> typing.Generator[tuple[tuple], None, None]:
    """Generator of the pairs of elements in a list"""
    for i, a in enumerate(singles):
        for b in singles[(i+1):]:
            yield a, b
            if reverse:
                yield b, a

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
        for a, b in find_pairs(freq, True):
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            nx = dx + b[0]
            ny = dy + b[1]
            if is_in_bounds(nx, ny, antinodes):
                if antinodes[ny][nx] != "#":
                    antinodes[ny][nx] = "#"
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
