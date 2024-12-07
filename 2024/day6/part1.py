DIRS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

def find_guard(spaces:list[list[str]]) -> tuple[int,int,str]:
    for y, line in enumerate(spaces):
        for x, space in enumerate(line):
            if space in ["^", ">", "v", "<"]:
                return x, y, space
    return -1, -1, "^"

def to_obstacle(spaces:list[list[str]], guard:tuple[int,int,str]) -> tuple[int,int,str]:
    x = guard[0]
    y = guard[1]
    direc = guard[2]
    while True:
        x_p = x
        y_p = y
        x += DIRS[direc][0]
        y += DIRS[direc][1]
        try:
            if x < 0 or y < 0:
                raise IndexError
            spaces[y_p][x_p] = "x"
            if spaces[y][x] == "#":
                new_guard = (x_p, y_p, guard[2])
                spaces[new_guard[1]][new_guard[0]] = guard[2]
                return rotate_guard(spaces, new_guard)
        except IndexError:
            return (-1, -1, guard[2])

def rotate_guard(spaces:list[list[str]], guard:tuple[int,int,str]) -> None:
    guards = list(DIRS.keys())
    x = guard[0]
    y = guard[1]
    direc = guard[2]
    curr = guards.index(direc)
    next_ = (curr + 1) % len(guards)
    spaces[y][x] = guards[next_]
    return guard[0], guard[1], guards[next_]

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    spaces = [list(line) for line in content]

    guard = find_guard(spaces)
    while guard[0] != -1:
        guard = to_obstacle(spaces, guard)

    unique = 0
    for line in spaces:
        unique += line.count("x")

    print(unique)

if __name__ == "__main__":
    main()
    # 5531
