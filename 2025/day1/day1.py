FILENAME = "test.txt"

class Dial: # pylint: disable= C0115
    def __init__(self, initial_position:int=0, positions:int=100):
        self._pos = initial_position
        self._positions = positions

    def __eq__(self, equalto):
        return self._pos == equalto

    def left(self, value:int):
        """Rotate the dial toward lower numbers."""
        # ignore starting on zero
        zeros = -int(self == 0)

        self._pos -= value
        while self._pos < 0:
            self._pos += self._positions
            zeros += 1

        # include ending on a zero
        return zeros + int(self == 0)

    def right(self, value:int):
        """Rotate the dial toward higher numbers."""
        zeros = 0

        self._pos += value
        while self._pos >= self._positions:
            self._pos -= self._positions
            zeros += 1

        return zeros

def part_1(): # pylint: disable= C0116
    dial = Dial(50, 100)
    counter = 0

    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        lr = line[0].lower()
        num = int(line[1:])

        if lr == "r":
            dial.right(num)
        else:
            dial.left(num)

        if dial == 0:
            counter += 1

    return counter

def part_2(): # pylint: disable= C0116
    dial = Dial(50, 100)
    counter = 0

    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        lr = line[0].lower()
        num = int(line[1:])

        if lr == "r":
            counter += dial.right(num)
        else:
            counter += dial.left(num)

    return counter

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
