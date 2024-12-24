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

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

def coord_diff(a:tuple[int,int], b:tuple[int,int]) -> tuple[int,int]:
    """a - b"""
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x, y

@lru_cache(maxsize=None)
def robot(moves:str, depth:int, keypad:hashabledict[str,tuple[int,int]]) -> str:
    """recursive find optimal path"""
    # exit condition
    if depth == 0:
        return moves

    x, y = keypad["A"]
    pattern = ""

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
            pattern += robot(y_first, depth - 1, hashabledict(keypad_directional))
        elif (x, y + dy) not in keypad.values():
            # applying y first puts robot over empty
            pattern += robot(x_first, depth - 1, hashabledict(keypad_directional))
        else:
            # either could be applied first, find the optimal one
            option_1 = robot(x_first, depth - 1, hashabledict(keypad_directional))
            option_2 = robot(y_first, depth - 1, hashabledict(keypad_directional))
            pattern += min(option_1, option_2)

        # update position
        x, y = x_n, y_n
    return pattern

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        codes = f.read().split("\n")

    STAGES = 2

    complexities = 0
    for depth in range(STAGES + 2):
        complexities = 0
        for code in codes:
            moves = robot(code, depth, hashabledict(keypad_numeric))
            length = len(moves)
            number = int(code.removesuffix("A"))
            complexities += length * number

    print(complexities)

if __name__ == "__main__":
    main()
    # 219254
