DIRS = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}

def scan_for_empty(warehouse:list[list[str]], position:tuple[int,int], movement:tuple[int,int]) -> tuple[int,int]:
    """find coordinates of next empty space. returns `(-1, -1)` if impossible."""
    x, y = position
    while True:
        x += movement[0]
        y += movement[1]
        space = warehouse[y][x]
        if space == "#":
            # boxes stacked, return invalid
            return (-1, -1)
        if space == ".":
            # free to move boxes here
            return x, y

def try_move(warehouse:list[list[str]], robot:tuple[int,int], direction:str) -> tuple[int,int]:
    """try to move robot, returns new robot coordinates."""
    direc = DIRS[direction]
    x, y = robot
    x_c = x + direc[0]
    y_c = y + direc[1]

    space = warehouse[y_c][x_c]
    if space == ".":
        # immediate space is free, go there
        warehouse[y][x] = "."
        warehouse[y_c][x_c] = "@"
        return x_c, y_c

    if space == "#":
        # immediate space is occupied, do not move
        return x, y

    next_free = scan_for_empty(warehouse, robot, direc)
    if next_free == (-1, -1):
        # no valid moves
        return x, y

    # move the robot and boxes
    x_n, y_n = next_free
    warehouse[y][x] = "."
    warehouse[y_n][x_n] = "O"
    warehouse[y_c][x_c] = "@"
    return x_c, y_c

def find_in(warehouse:list[list[str]], item:str) -> list[tuple[int,int]]:
    """find all box coordinates."""
    boxes = []
    for y, line in enumerate(warehouse):
        for x, space in enumerate(line):
            if space == item:
                boxes.append((x, y))
    return boxes

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read()
        warehouse, moves = content.split("\n\n", maxsplit=1)

    warehouse = [list(line) for line in warehouse.split("\n")]
    moves = list(moves.replace("\n", ""))

    robot = find_in(warehouse, "@")[0]

    for move in moves:
        robot = try_move(warehouse, robot, move)

    boxes = find_in(warehouse, "O")
    score = sum(map(lambda b: b[0] + 100 * b[1], boxes))
    print(score)

if __name__ == "__main__":
    main()
    # 1559280
