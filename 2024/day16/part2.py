class Branch:
    def __init__(
            self,
            start:tuple[int,int],
            direction:tuple[int,int],
            visited:list[int],
            moves:int,
            turns:int
        ) -> None:
        self.start = start
        self.direction = direction
        self.position = self.start
        self.moves = moves
        self.turns = turns
        self.visited = visited.copy()

    def visit(self, coord:list[int,int]) -> None:
        """visit a node"""
        self.visited.extend(coord)

    def has_visited(self, coord:list[int,int]) -> bool:
        """check if node has been visited"""
        for pair in zip(self.visited[::2], self.visited[1::2]):
            if pair == coord:
                return True
        return False

    def visited_pairs(self) -> set[tuple[int,int]]:
        """get all visited coords as a set of tuples"""
        return set(zip(self.visited[::2], self.visited[1::2]))

def add_coords(a:list[int,int], b:list[int,int]) -> list[int,int]:
    """add x and y values of coordinates."""
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y

def maze_fetch(maze:list[str], pos:list[int,int]) -> str:
    """get item from maze coordinate"""
    x, y = pos
    return maze[y][x]

def breadth_first_linear_search(
        maze:list[str],
        start:tuple[int,int],
        end:tuple[int,int],
    ) -> set[tuple[int,int]]:
    """solve maze using minimal turns."""
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    queue = [Branch(start, directions[0], list(start), 0, 0)]

    ideal_branches:set[Branch] = set()
    reached_end = False

    while True:
        # could not solve
        if len(queue) == 0:
            break

        # get next branch from queue
        branch = queue.pop()

        # find left and right offsets
        dir_idx = directions.index(branch.direction)
        left_right = [directions[(dir_idx + 1) % 4], directions[(dir_idx - 1) % 4]]

        # keep moving forward until hit wall
        while True:
            # if the end if found, do not branch
            if not reached_end:
                # check left and right for options
                for lr in left_right:
                    lr_check = add_coords(branch.position, lr)
                    lr_item = maze_fetch(maze, lr_check)
                    if lr_item != "#":
                        if branch.has_visited(lr_check):
                            continue
                        new_branch_start = add_coords(lr_check, lr)
                        new_branch_moves = branch.moves + 2
                        new_branch_turns = branch.turns + 1

                        # create a new branch to the side
                        new_branch = Branch(new_branch_start, lr, branch.visited, new_branch_moves, new_branch_turns)
                        new_branch.visit(lr_check)
                        new_branch.visit(new_branch_start)

                        # if the branch is the end, no need to add it to the queue
                        if new_branch_start == end:
                            ideal_branches.add(new_branch)
                            reached_end = True
                        else:
                            # add new branch to back of queue
                            queue.insert(0, new_branch)

            # check able to move forward
            ahead_start = add_coords(branch.position, branch.direction)
            ahead_item = maze_fetch(maze, ahead_start)
            if ahead_item == "#":
                break

            # move forward 2 spaces
            branch.position = add_coords(branch.position, branch.direction)
            branch.visit(branch.position)
            branch.position = add_coords(branch.position, branch.direction)
            branch.visit(branch.position)
            branch.moves += 2

            # check if reached the end
            if branch.position == end:
                ideal_branches.add(branch)
                reached_end = True

    lengths = [branch.moves for branch in ideal_branches]
    min_length = min(lengths)

    ideal_spaces = set()
    for ideal_branch in ideal_branches:
        if ideal_branch.moves > min_length:
            continue
        #print(ideal_branch.visited_pairs())
        for visit in ideal_branch.visited_pairs():
            ideal_spaces.add(visit)
    return ideal_spaces

def print_maze(maze:list[str], visited:set[tuple[int,int]]) -> None:
    maze_list = [list(line) for line in maze]
    for x, y in visited:
        maze_list[y][x] = "O"
    maze_print = ["".join(line) for line in maze_list]
    print(*maze_print, sep="\n")

def main():
    with open("test.txt", "r", encoding="utf-8") as f:
        maze = f.read().split("\n")

    start = (1, len(maze)-2)
    end = (len(maze[0])-2, 1)

    on_ideal_path = breadth_first_linear_search(maze, start, end)

    print_maze(maze, on_ideal_path)

    print("\non ideal path:")
    print(on_ideal_path)
    print(len(on_ideal_path))

if __name__ == "__main__":
    main()
    #
