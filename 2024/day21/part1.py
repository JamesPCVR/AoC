class Robot:
    def __init__(self, keypad:dict[str,tuple[int,int]]) -> None:
        self.keypad = keypad
        self.position = keypad["A"]

    def coord_diff(self, a:tuple[int,int], b:tuple[int,int]) -> tuple[int,int]:
        """a - b"""
        x = a[0] - b[0]
        y = a[1] - b[1]
        return x, y

    def type_sequence(self, sequence:str) -> str:
        pattern = ""
        for seq in sequence:
            coord = self.keypad[seq]
            delta = self.coord_diff(coord, self.position)
            pattern += self.shortest_avoid_empty(delta)
            self.position = coord
            pattern += "A"
        return pattern

    def shortest_avoid_empty(self, delta:tuple[int,int]) -> str:
        """return path avoiding empty squares"""
        dx, dy = delta
        pattern = ""
        corner = (self.position[0] + dx, self.position[1])
        if corner in self.keypad.values():
            # x first then y
            pattern += ("<" if dx < 0 else ">") * abs(dx)
            pattern += ("^" if dy < 0 else "v") * abs(dy)
        else:
            # y first then x
            pattern += ("^" if dy < 0 else "v") * abs(dy)
            pattern += ("<" if dx < 0 else ">") * abs(dx)
        return pattern

def main():
    with open("test.txt", "r", encoding="utf-8") as f:
        codes = f.read().split("\n")

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

    robots = [
        Robot(keypad_numeric),
        Robot(keypad_directional),
        Robot(keypad_directional)
    ]

    complexities = []
    for code in codes:
        sequence = code
        print(sequence)
        for robot in robots:
            sequence = robot.type_sequence(sequence)
            print(sequence)

        # find complexity
        length = len(sequence)
        number = int(code.removesuffix("A"))
        complexity = length * number
        complexities.append(complexity)
        print(length, number, complexity)
        print()

    print(sum(complexities))

if __name__ == "__main__":
    main()
    # 223838 too high
