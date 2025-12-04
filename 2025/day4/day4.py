from copy import deepcopy

FILENAME = "test.txt"

def get_bounded(grid:list[list[str]], x:int, y:int):
    """Get element from list and default character if our of range."""
    if x < 0 or x >= len(grid[0]):
        return '.'
    if y < 0 or y >= len(grid):
        return '.'

    return grid[y][x]

def get_neighbours(grid:list[list[str]], x:int, y:int):
    """Get the neighbours of a cell in the grid."""
    positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    return str([get_bounded(grid, x+xi, y+yi) for xi, yi in positions])

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    accessible = 0
    for yi, y in enumerate(grid):
        for xi, x in enumerate(y):
            if x != '@':
                continue

            count = get_neighbours(grid, xi, yi).count('@')
            accessible += count < 4

    return accessible

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        new_grid = [list(line.strip()) for line in f.readlines()]

    all_removed = 0
    while True:
        removed = 0
        old_grid = deepcopy(new_grid)
        for yi, y in enumerate(old_grid):
            for xi, x in enumerate(y):
                if x != '@':
                    continue

                count = get_neighbours(old_grid, xi, yi).count('@')
                if count < 4:
                    new_grid[yi][xi] = 'X'
                    removed += 1

        if removed == 0:
            break
        all_removed += removed

    return all_removed

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
