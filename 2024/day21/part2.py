from functools import lru_cache

keypad_directional = {
                 "^": (1, 0), "A": (2, 0),
    "<": (0, 1), "v": (1, 1), ">": (2, 1)
}

keypad_numeric = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
                 "0": (1, 3), "A": (2, 3)
}

def coord_diff(a:tuple[int,int], b:tuple[int,int]) -> tuple[int,int]:
    """a - b"""
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x, y

def robot(moves:str, depth:int, keypad:dict[str,tuple[int,int]]) -> int:
    """recursive find optimal path length"""
    # exit condition
    if depth == 0:
        return len(moves)

    x, y = keypad["A"]
    pattern_length = 0

    for step in moves:
        x_n, y_n = keypad[step]
        dx = x_n - x
        dy = y_n - y

        # required moves to reach `x_n`, `y_n`
        str_x = ("<" if dx < 0 else ">") * abs(dx)
        str_y = ("^" if dy < 0 else "v") * abs(dy)
        x_first = str_x + str_y + "A"
        y_first = str_y + str_x + "A"

        if (x + dx, y) not in keypad.values():
            # applying x first puts robot over empty
            pattern_length += robot_directional(y_first, depth - 1)
        elif (x, y + dy) not in keypad.values():
            # applying y first puts robot over empty
            pattern_length += robot_directional(x_first, depth - 1)
        else:
            # either could be applied first, find the optimal one
            option_1 = robot_directional(x_first, depth - 1)
            option_2 = robot_directional(y_first, depth - 1)
            pattern_length += min(option_1, option_2)

        # update position
        x, y = x_n, y_n
    return pattern_length

@lru_cache(maxsize=None)
def robot_directional(moves:str, depth:int) -> int:
    """recursive optimal path length for directional keypad"""
    return robot(moves, depth, keypad_directional)

def robot_numeric(moves:str, depth:int) -> int:
    """recursive optimal path length for numeric keypad"""
    return robot(moves, depth, keypad_numeric)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        codes = f.read().split("\n")

    STAGES = 25

    complexities = 0
    for code in codes:
        length = robot_numeric(code, STAGES + 1)
        number = int(code.removesuffix("A"))
        complexities += length * number

    print(complexities)

if __name__ == "__main__":
    main()
