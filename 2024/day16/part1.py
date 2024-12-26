class Branch:
    def __init__(
            self,
            start:tuple[int,int],
            direction:tuple[int,int],
            moves:int,
            turns:int
        ) -> None:
        self.start = start
        self.direction = direction
        self.moves = moves
        self.turns = turns

def add_coords(*a:tuple[int,int]) -> tuple[int,int]:
    """add x and y values of coordinates."""
    x = sum(xy[0] for xy in a)
    y = sum(xy[1] for xy in a)
    return x, y

def maze_fetch(maze:list[str], pos:tuple[int,int]) -> str:
    """get item from maze coordinate"""
    x, y = pos
    return maze[y][x]

def breadth_first_linear_search(
        maze:list[str],
        start:tuple[int,int],
        end:tuple[int,int],
    ) -> tuple[int,int]:
    """solve maze using minimal turns."""
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    queue = [Branch(start, directions[0], 0, 0)]
    queued = set()
    queued.add(start)
    visited = set()

    while True:
        # could not solve
        if len(queue) == 0:
            break

        # get next branch from queue
        branch = queue.pop()
        queued.remove(branch.start)
        visited.add(branch.start)

        # find left and right offsets
        dir_idx = directions.index(branch.direction)
        left_right = [directions[(dir_idx + 1) % 4], directions[(dir_idx - 1) % 4]]

        # keep moving forward until hit wall
        while True:
            # check left and right for options
            for lr in left_right:
                lr_check = add_coords(branch.start, lr)
                lr_item = maze_fetch(maze, lr_check)
                if lr_item != "#":
                    new_branch_start = add_coords(lr_check, lr)
                    if new_branch_start in visited or new_branch_start in queued:
                        continue
                    new_branch_moves = branch.moves + 2
                    new_branch_turns = branch.turns + 1
                    if new_branch_start == end:
                        return new_branch_moves, new_branch_turns
                    queue.insert(0, Branch(new_branch_start, lr, new_branch_moves, new_branch_turns))
                    queued.add(new_branch_start)

            # check able to move forward
            ahead_start = add_coords(branch.start, branch.direction)
            ahead_item = maze_fetch(maze, ahead_start)
            if ahead_item == "#":
                break

            # move forward 2 spaces
            branch.start = add_coords(branch.start, branch.direction, branch.direction)
            branch.moves += 2
            if branch.start == end:
                return branch.moves, branch.turns

    # could not solve
    return -1, -1

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        maze = f.read().split("\n")

    start = (1, len(maze)-2)
    end = (len(maze[0])-2, 1)

    shortest_weight = breadth_first_linear_search(maze, start, end)

    print(shortest_weight[1] * 1000 + shortest_weight[0])

if __name__ == "__main__":
    main()
    # 83444
