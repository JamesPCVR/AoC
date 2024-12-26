class Node:
    def __init__(
            self,
            start:tuple[int,int],
            direction:tuple[int,int],
            score:int
        ) -> None:
        self.start = start
        self.direction = direction
        self.score = score

    def left(self) -> tuple[int,int]:
        return directions[(directions.index(self.direction) + 1) % 4]

    def right(self) -> tuple[int,int]:
        return directions[(directions.index(self.direction) - 1) % 4]

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def add_coords(a:list[int,int], b:list[int,int]) -> list[int,int]:
    """add x and y values of coordinates."""
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y

def maze_fetch(maze:list[str], pos:list[int,int]) -> str:
    """get item from maze coordinate"""
    x, y = pos
    return maze[y][x]

def breadth_first_search(
        maze:list[str],
        start:tuple[int,int]
    ) -> list[list[int]]:
    """solve maze using minimal turns."""
    scores = [[-1]*len(maze[0]) for _ in maze]
    scores[start[1]][start[0]] = 0

    queue = [Node(start, directions[0], 0)]

    while len(queue) > 0:
        current_node = queue.pop()

        options = [
            (current_node.left(), current_node.score + 1001),
            (current_node.direction, current_node.score + 1),
            (current_node.right(), current_node.score + 1001)
        ]

        for check_dir, check_score in options:
            check_pos = add_coords(current_node.start, check_dir)
            space = maze_fetch(maze, check_pos)

            if space == "#":
                continue
            if check_pos == start:
                continue

            if maze_fetch(scores, check_pos) == -1 or check_score < maze_fetch(scores, check_pos):
                scores[check_pos[1]][check_pos[0]] = check_score
                queue.insert(0, Node(check_pos, check_dir, check_score))

    return scores

def reverse_breadth_first_search(
        scores:list[list[int]],
        end:tuple[int,int]
    ) -> set[tuple[int,int]]:
    """find all spaces on ideal path"""
    ideal_spaces = set()
    ideal_spaces.add(end)
    queue = [
        Node(end, directions[2], maze_fetch(scores, end)),
        Node(end, directions[3], maze_fetch(scores, end))
    ]
    while len(queue) > 0:
        current_node = queue.pop()

        options = [
            (current_node.left(), current_node.score - 1001),
            (current_node.direction, current_node.score - 1),
            (current_node.right(), current_node.score - 1001)
        ]

        for check_dir, check_score in options:
            check_pos = add_coords(current_node.start, check_dir)
            space = maze_fetch(scores, check_pos)

            if space == -1:
                continue
            if check_pos in ideal_spaces:
                continue
            if maze_fetch(scores, check_pos) in [check_score-1000, check_score]:
                queue.append(Node(check_pos, check_dir, check_score))
                ideal_spaces.add(check_pos)

    return ideal_spaces

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        maze = f.read().split("\n")

    start = (1, len(maze)-2)
    end = (len(maze[0])-2, 1)

    scores = breadth_first_search(maze, start)
    on_ideal_path = reverse_breadth_first_search(scores, end)

    print(len(on_ideal_path))

if __name__ == "__main__":
    main()
    # 483
