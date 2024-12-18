def breadth_first_search(memory:list[list[str]], start:tuple[int,int], end:tuple[int,int]) -> int:
    """find shortest path."""
    queue = [(start, 0)]
    queued = set()
    queued.add(start)
    visited = set()
    neighbours = [
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1),
    ]
    size = len(memory) - 1
    while True:
        (x, y), weight = queue.pop()
        queued.remove((x, y))
        visited.add((x, y))
        for x_s, y_s in neighbours:
            x_c = x + x_s
            y_c = y + y_s
            if (x_c, y_c) in visited:
                continue
            if not 0 <= x_c <= size:
                continue
            if not 0 <= y_c <= size:
                continue
            if memory[y_c][x_c] != ".":
                continue
            if (x_c, y_c) in queued:
                continue
            if (x_c, y_c) == end:
                return weight + 1
            queue.insert(0, ((x_c, y_c), weight + 1))
            queued.add((x_c, y_c))

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        size, simulate, program = f.read().split("\n", maxsplit=2)
        size = int(size)
        simulate = int(simulate)

    incoming = [tuple(map(int, byte.split(","))) for byte in program.split("\n")[:simulate]]

    memory = [list("." * (size + 1)) for _ in range(size + 1)]
    start = (0,0)
    end = (size, size)

    for x, y in incoming:
        memory[y][x] = "#"

    shortest_weight = breadth_first_search(memory, start, end)

    print(shortest_weight)

if __name__ == "__main__":
    main()
    # 506
