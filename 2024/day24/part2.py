from PIL import Image, ImageDraw

HORIZ_SPACING = 40

VERT_SPACING = 10

IMAGE_SIZE = (HORIZ_SPACING * 46, VERT_SPACING * 180)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        start_states, gates = f.read().split("\n\n", maxsplit=1)

    start_states = start_states.split("\n")
    gates = set(gates.split("\n"))

    print(gates)

    # wires holds coordinate of wire start
    wires = {}
    for wire in start_states:
        name, _ = wire.split(": ", maxsplit=1)
        n = int(name[1:])
        wires[name] = (
            IMAGE_SIZE[0] - int((n+0.5) * HORIZ_SPACING) + (-10 if name[0] == "y" else 0),
            VERT_SPACING
        )

    solved_gates = set()
    gate_positions = set()

    img = Image.new("RGBA", IMAGE_SIZE, (255, 255, 255, 255))
    img_and = Image.open("assets/and.png")
    img_or = Image.open("assets/or.png")
    img_xor = Image.open("assets/xor.png")
    draw = ImageDraw.Draw(img)

    while to_solve := gates.difference(solved_gates):
        # while there are still gates to solve
        for gate in to_solve:
            parts = gate.split(" ")
            a, op, b, _, out = parts
            if not (a in wires and b in wires):
                # cannot place gate yet
                continue
            position = (
                int((wires[a][0] + wires[b][0]) // 2),
                max(wires[a][1], wires[b][1]) + VERT_SPACING
            )
            while position in gate_positions:
                position = (position[0] - 15, position[1])
            gate_positions.add(position)
            if op == "AND":
                img.paste(img_and, position, img_and)
            elif op == "OR":
                img.paste(img_or, position, img_or)
            elif op == "XOR":
                img.paste(img_xor, position, img_xor)
            draw.line(wires[a] + (position[0]+2, position[1]), fill = 128)
            draw.line(wires[b] + (position[0]+8, position[1]), fill = 128)
            wires[out] = (position[0] + 4, position[1] + 10)
            if out[0] == "z":
                n = int(out[1:])
                end = (
                    IMAGE_SIZE[0] - int((n+0.5) * HORIZ_SPACING),
                    IMAGE_SIZE[1] - VERT_SPACING
                )
                draw.line(wires[out] + end, fill = 128)
            solved_gates.add(gate)

    img.save("output.png")
    img_and.close()
    img_or.close()
    img_xor.close()

if __name__ == "__main__":
    main()
    # bit 11 has issue (qff qnw)
    # z16 and and xor output swapped (z16 pbv)
    # z23 or and xor output swapped (z23 qqp)
    # z36 and and xor output swapped (fbq z36)
    # fbq,pbv,qff,qnw,qqp,z16,z23,z36
