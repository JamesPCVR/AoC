FILENAME = "in.txt"

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()[::2]]

    lines[0] = lines[0].replace("S", "|")
    lines = list(map(list, lines))

    splits = 0
    for index in range(1, len(lines)):
        line = lines[index]
        prev_line = lines[index - 1]
        splitter_indexes = [i for i, s in enumerate(line) if s == "^"]
        has_beam = [prev_line[i] == "|" for i in splitter_indexes]
        for i, s in enumerate(line):
            if prev_line[i] != "|":
                continue
            if s == "^":
                lines[index][i-1] = "|"
                lines[index][i+1] = "|"
                continue
            if s == ".":
                lines[index][i] = "|"
                continue

        splits += sum(has_beam)

        # print("".join(lines[index]))

    return splits

def formatter(string:str): # pylint: disable= C0116
    if string == ".":
        return 0
    if string == "S":
        return 1
    try:
        return int(string)
    except ValueError:
        return string

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()[::2]]

    lines = [list(map(formatter, line)) for line in map(list, lines)]

    for index in range(1, len(lines)):
        line = lines[index]
        prev_line = lines[index - 1]
        for i, (space, beam_time) in enumerate(zip(line, prev_line)):
            if beam_time in (0, "^"):
                continue
            if space == "^":
                lines[index][i-1] += beam_time
                lines[index][i+1] += beam_time
                continue
            lines[index][i] += beam_time

    timelines = sum(
        beam_time
        for beam_time in lines[-1]
        if isinstance(beam_time, int)
    )

    return timelines

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
