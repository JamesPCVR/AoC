from copy import deepcopy

class Branch:
    def __init__(
            self,
            start:tuple[int,int],
            direction:tuple[int,int],
            visited:set[tuple[int,int]],
            moves:int,
            turns:int
        ) -> None:
        self.start = start
        self.direction = direction
        self.position = self.start
        self.moves = moves
        self.turns = turns
        self.visited = deepcopy(visited)

    def visit(self, coord:tuple[int,int]) -> None:
        """visit a node"""
        self.visited.add(coord)

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

    start_set = set()
    start_set.add(start)

    queue = [Branch(start, directions[0], start_set, 0, 0)]

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
                        if lr_check in branch.visited:# or lr_check in queued:
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
            branch.visited.add(add_coords(branch.position, branch.direction))
            branch.position = add_coords(branch.position, branch.direction, branch.direction)
            branch.visited.add(branch.position)
            branch.moves += 2
            if branch.position == end:
                ideal_branches.add(branch)
                reached_end = True

    ideal_spaces = set()
    for ideal_branch in ideal_branches:
        print(ideal_branch.visited)
        for visit in ideal_branch.visited:
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
