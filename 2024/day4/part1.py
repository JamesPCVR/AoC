import os
os.system("")

def check_star(x:int, y:int, crossword:list[str]) -> list[tuple[tuple[int,int],tuple[int,int]]]:
    steps = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]

    lim_x_neg = 0
    lim_x_pos = len(crossword[0])
    lim_y_neg = 0
    lim_y_pos = len(crossword)

    matches = []
    for direc in steps:
        string = ""
        for i in range(4):
            x_c = x + direc[0]*i
            y_c = y + direc[1]*i

            if lim_x_neg > x_c or x_c >= lim_x_pos:
                continue
            if lim_y_neg > y_c or y_c >= lim_y_pos:
                continue

            string += crossword[y_c][x_c]

        if string == "XMAS":
            matches.append(((x,y), (x_c, y_c)))
        elif string == "SAMX":
            matches.append(((x_c ,y_c), (x,y)))

    return matches

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    words = []
    for y, line in enumerate(lines):
        for x in range(len(line)):
            words.extend(check_star(x, y, lines))

    words_set = sorted(list(set(words)))
    print(len(words_set))

if __name__ == "__main__":
    main()
