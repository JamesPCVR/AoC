import numpy as np

FILENAME = "test.txt"

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

if __name__ == "__main__":
    mech = get_machines()
    print(f"part 1: {part_1(mech)}")
