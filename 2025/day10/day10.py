import sympy as sp

FILENAME = "in.txt"

class Machine: # pylint: disable= C0115
    def __init__(
            self,
            light_target:list[bool],
            buttons:list[tuple[int]],
            joltages:list[int]
        ):
        self.target = light_target
        self.buttons = buttons
        self.joltages = joltages

    def __repr__(self):
        state = "".join("#" if on else "." for on in self.target)
        return f"Machine({state})"

class State: # pylint: disable= C0115
    def __init__(self, state:list[bool], presses:list[int], last_press:int):
        self.state = state
        self.presses = presses.copy()
        self.last_press = last_press

def get_machines(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    machines = []
    for line in lines:
        line_split = line.strip().split(" ")
        l = [c == "#" for c in line_split[0][1:-1]]
        b = [tuple(map(int, button[1:-1].split(","))) for button in line_split[1:-1]]
        j = list(map(int, line_split[-1][1:-1].split(",")))
        machines.append(Machine(l, b, j))

    return machines

def press_button(state:list[bool], wires:list[int]):
    """Toggle the lights connected to the wires."""
    new_state = state.copy()
    for wire in wires:
        new_state[wire] ^= True
    return new_state

def find_button_presses(machine:Machine):
    """Find the minimum number of button presses to reach a target sequence."""
    target = machine.target
    state = [False for _ in target]
    buttons = machine.buttons

    queue = [State(state, [0 for _ in buttons], 0)]

    while True:
        # could not solve
        if len(queue) == 0:
            break

        state = queue.pop(0)

        for i, button in enumerate(buttons[state.last_press:]):
            new_state = State(press_button(state.state, button), state.presses, i)
            new_state.presses[i] += 1
            if new_state.state == target:
                return new_state.presses
            queue.append(new_state)

    return []

def part_1(machines:list[Machine]): # pylint: disable= C0116
    total_presses = 0
    for machine in machines:
        presses = find_button_presses(machine)
        clicks = sum(presses)
        total_presses += clicks

    return total_presses

def is_positive_int(num:float):
    if num < 0:
        return False

    if num - int(num) != 0:
        return False

    return True

# def minimum_sum_solution(
#         sol:sp.Matrix,
#         params:sp.Matrix,
#         top:int=50
#     ) -> sp.Matrix:
#     min_sum = 1000000000 # definitely a better solution than this
#     min_sol = sp.zeros(len(sol), 1)

#     for idx in range(top ** len(params)):
#         taus = {tau: idx//(top**ti)%top for ti, tau in enumerate(params)}
#         sol_unique = sol.xreplace(taus)
#         if any(not is_positive_int(cell) for cell in sol_unique):
#             continue
#         sol_sum = sum(sol_unique)
#         if sol_sum < min_sum:
#             min_sum = sol_sum
#             min_sol = sol_unique

#     return min_sol

def minimum_sum_solution(
        sol:sp.Matrix,
        params:sp.Matrix
    ):
    taus = {tau:0 for tau in params}
    best_sol = sol.xreplace(taus)
    start_sum = sum(best_sol)
    for tau in params:
        # increment tau
        taus[tau] += 1
        new_sol = sol.xreplace(taus)
        new_sum = sum(new_sol)
        # if it did not decrease the sum, revert and move on
        if new_sum >= start_sum:
            taus[tau] -= 1
            continue
        # if it reduced the sum continue until it is invalid

        while True:
            new_sol = sol.xreplace(taus)

            # cannot have negative presses
            if any(num < 0 for num in new_sol):
                taus[tau] -= 1
                break

            # skip non-integers
            if all((num - int(num)) == 0 for num in new_sol):
                best_sol = new_sol

            taus[tau] += 1

    return best_sol

def part_2(machines:list[Machine]):
    total_presses = 0
    for mi, machine in enumerate(machines):
        print(f"{mi:3d}/{len(machines)} {machine}", end=" ")
        buttons = machine.buttons
        joltages = machine.joltages

        # create the system of equations
        button_map = [[0]*len(buttons) for _ in joltages]
        for j, button in enumerate(buttons):
            for i, wire in enumerate(button):
                button_map[wire][j] = 1
        m = sp.Matrix(button_map)
        t = sp.Matrix(joltages)

        # solve the system parametrically
        sol, params = m.gauss_jordan_solve(t)

        # add exact solution or solve parametric solution
        print(len(params), end=" ")
        if len(params) == 0:
            s = sum(sol)
            total_presses += s
            print(s)
        else:
            sol_u = minimum_sum_solution(sol, params)
            s = sum(sol_u)
            total_presses += s
            print(sol_u, end=" ")
            print(s)

    return total_presses

if __name__ == "__main__":
    mech = get_machines()
    # print(f"part 1: {part_1(mech)}")
    print(f"part 2: {part_2(mech)}") # 17425 too low
