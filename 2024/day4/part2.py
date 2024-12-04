def check_star(x:int, y:int, crossword:list[str]) -> list[tuple[tuple[int,int],tuple[int,int]]]:
    steps = [
        (-1, 1),
        (1, 1),
        (-1, -1),
        (1, -1)
    ]

    lim_x_neg = 1
    lim_x_pos = len(crossword[0]) - 1
    lim_y_neg = 1
    lim_y_pos = len(crossword) - 1

    if lim_x_neg > x or x >= lim_x_pos:
        return []
    if lim_y_neg > y or y >= lim_y_pos:
        return []

    matches = []
    string = ""
    for direc in steps:
        x_c = x + direc[0]
        y_c = y + direc[1]
        string += crossword[y_c][x_c]

    if string in ["MMSS", "MSMS", "SMSM", "SSMM"]:
        matches.append((x,y))

    return matches

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    words = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A":
                words.extend(check_star(x, y, lines))

    print(len(words))

if __name__ == "__main__":
    main()
