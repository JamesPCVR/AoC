DIRS = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}

def check_boxes_moveable(warehouse:list[list[str]], start:tuple[int,int], movement:tuple[int,int]) -> bool:
    """check the series of boxes can move withoug issue."""
    x, y = start
    c = warehouse[y][x]

    # space is empty
    if c == ".":
        return True

    # space is a wall
    if c == "#":
        return False

    # find left and right coordinates
    if c == "[":
        x_left = x
        x_right = x + 1
    else:
        x_left = x - 1
        x_right = x

    if movement[0] == 0:
        # vertical movement
        x_left_next = x_left
        x_right_next = x_right
        y_next = y + movement[1]

        next_left = warehouse[y_next][x_left_next]
        if next_left == "[":
            # boxes are aligned
            return check_boxes_moveable(warehouse, (x_left_next, y_next), movement)
        # boxes are misaligned
        l = check_boxes_moveable(warehouse, (x_left_next, y_next), movement)
        r = check_boxes_moveable(warehouse, (x_right_next, y_next), movement)
        return l and r

    # horizontal movement
    x_left_next = x_left + (movement[0] * 2)
    x_right_next = x_right + (movement[0] * 2)
    y_next = y

    return check_boxes_moveable(warehouse, (x_left_next if movement[0] == 1 else x_right_next, y_next), movement)

def move_boxes(warehouse:list[list[str]], start:tuple[int,int], movement:tuple[int,int]) -> None:
    """recursive box movment, assumes move is possible."""
    x, y = start
    c = warehouse[y][x]

    # not a box, no need to move
    if c not in ["[", "]"]:
        return

    # find left and right coordinates
    if c == "[":
        x_left = x
        x_right = x + 1
    else:
        x_left = x - 1
        x_right = x

    if movement[0] == 0:
        # vertical movement
        x_left_next = x_left
        x_right_next = x_right
        y_next = y + movement[1]

        next_left = warehouse[y_next][x_left_next]
        if next_left == "[":
            # boxes are aligned
            move_boxes(warehouse, (x_left_next, y_next), movement)
        else:
            # boxes are misaligned
            move_boxes(warehouse, (x_left_next, y_next), movement)
            move_boxes(warehouse, (x_right_next, y_next), movement)

        # children moved, move self
        warehouse[y_next][x_left_next] = "["
        warehouse[y_next][x_right_next] = "]"
        warehouse[y][x_left] = "."
        warehouse[y][x_right] = "."
    else:
        # horizontal movement
        x_left_next = x_left + (movement[0] * 2)
        x_right_next = x_right + (movement[0] * 2)
        y_next = y
        if movement[0] == 1:
            # moving right, pick next (left)
            move_boxes(warehouse, (x_left_next, y_next), movement)

            # children moved, move self
            warehouse[y_next][x_right + 1] = "]"
            warehouse[y_next][x_left + 1] = "["
            warehouse[y_next][x_left] = "."
        else:
            # moving left, pick next (right)
            move_boxes(warehouse, (x_right_next, y_next), movement)

            # children moved, move self
            warehouse[y_next][x_left - 1] = "["
            warehouse[y_next][x_right - 1] = "]"
            warehouse[y_next][x_right] = "."

def try_move_boxes(warehouse:list[list[str]], start:tuple[int,int], movement:tuple[int,int]) -> bool:
    """try to move all boxes in a direction, return `True` if possible."""
    # step to the next box
    begin = tuple(a + b for a, b in zip(start, movement))
    can_move = check_boxes_moveable(warehouse, begin, movement)

    # move boxes if there is space
    if can_move:
        move_boxes(warehouse, begin, movement)
        warehouse[begin[1]][begin[0]] = "@"
        warehouse[start[1]][start[0]] = "."
    
    return can_move

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

    if try_move_boxes(warehouse, robot, direc):
        # boxes moved successfully, now move robot
        warehouse[y][x] = "."
        warehouse[y_c][x_c] = "@"
        return x_c, y_c

    # boxes fully stacked, so cannot move
    return x, y

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

    replace = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    for o, n in replace.items():
        warehouse = warehouse.replace(o, n)

    warehouse = [list(line) for line in warehouse.split("\n")]
    moves = list(moves.replace("\n", ""))

    robot = find_in(warehouse, "@")[0]

    for move in moves:
        robot = try_move(warehouse, robot, move)

    boxes = find_in(warehouse, "[")
    score = sum(map(lambda b: b[0] + 100 * b[1], boxes))
    print(score)

if __name__ == "__main__":
    main()
    # 1576353
