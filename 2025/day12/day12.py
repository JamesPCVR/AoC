import numpy as np

class Present:
    def __init__(self, shape:list[str]):
        self._weight = 0
        self.shape = shape

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        shape = [
            [x == "#" for x in y]
            for y in value
        ]
        self._shape = np.asarray(shape)
        self._weight = sum(sum(self._shape))

    @property
    def weight(self):
        return self._weight

    def __repr__(self):
        string = "Present:\n"
        for y in self.shape:
            for x in y:
                string += "#" if x else "."
            string += "\n"
        return string.strip()

class Tree:
    def __init__(self, width:int, length:int, presents:list[int]):
        self.width = width
        self.length = length
        self.presents = presents

    @property
    def size(self):
        return self.width * self.length

    def __repr__(self):
        return f"Tree({self.width}x{self.length}: {self.presents})"

def get_presents(filename:str):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().split("\n\n")

    # last element is the trees
    presents = []
    for line in lines[:-1]:
        line_split = line.split("\n")
        present = Present(line_split[1:])
        presents.append(present)

    trees = []
    for line in lines[-1].strip().split("\n"):
        line_split = line.split(": ", maxsplit=1)
        w, h = list(map(int, line_split[0].split("x", maxsplit=1)))
        p = tuple(map(int, line_split[1].split(" ")))
        trees.append(Tree(w, h, p))

    return presents, trees

def can_fit(presents:list[Present], tree:Tree):
    """Check if all the presents fit under the tree."""

    # check there is enough space assuming perfect packing
    volume = sum(
        presents[idx].weight * num
        for idx, num in enumerate(tree.presents)
    )
    if volume > tree.size:
        return False

    # check if they all fit next to each other without packing
    gridsize = (tree.width//3) * (tree.length//3)
    num_presents = sum(tree.presents)
    if gridsize >= num_presents:
        return True

    print("unknown")
    return False

def part_1(presents:list[Present], trees:list[Tree]): # pylint: disable= C0116
    return sum(
        can_fit(presents, tree)
        for tree in trees
    )

if __name__ == "__main__":
    presents, trees = get_presents("in.txt")
    print(f"part 1: {part_1(presents, trees)}")
