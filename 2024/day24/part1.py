def solve_gate(wires:dict[str,int], expression:str) -> bool:
    """solve expression and put result in wires"""
    parts = expression.split(" ")
    a, operation, b, _, output = parts
    if not (a in wires and b in wires):
        return False
    a_value = wires[a]
    b_value = wires[b]
    if operation == "AND":
        result = a_value and b_value
    elif operation == "OR":
        result = a_value or b_value
    elif operation == "XOR":
        result = int(a_value != b_value)
    else:
        result = 0
    wires[output] = result
    return True

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        start_states, gates = f.read().split("\n\n", maxsplit=1)

    start_states = start_states.split("\n")
    gates = set(gates.split("\n"))

    print(start_states)
    print(gates)

    wires = {}
    for wire in start_states:
        name, state = wire.split(": ", maxsplit=1)
        wires[name] = int(state)

    print(wires)

    solved_gates = set()

    while to_solve := gates.difference(solved_gates):
        # while there are still gates to solve
        for gate in to_solve:
            if solve_gate(wires, gate):
                solved_gates.add(gate)

    print(wires)

    binary = list("0" * 64)
    for name, state in wires.items():
        if name[0] != "z":
            continue
        if not state:
            continue
        n = int(name[1:])
        binary[-n-1] = "1"

    print("".join(binary))

    print(int("0b" + "".join(binary), 2))

if __name__ == "__main__":
    main()
    # 49430469426918
