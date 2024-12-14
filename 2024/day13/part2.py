import re
import numpy as np

def is_int(num:np.float32) -> bool:
    """check if float could be int."""
    tol = abs(num - round(num))
    return tol < 0.0001

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read()
        x = re.findall(r"(?<=X\+)\d{2}(?=,)", content)
        y = re.findall(r"(?<=Y\+)\d{2}(?=\n)", content)
        x_t = re.findall(r"(?<=X=)\d{3,5}(?=,)", content)
        y_t = re.findall(r"(?<=Y=)\d{3,5}", content)

    total_cost = 0

    for i in range(len(x_t)): # pylint: disable=C0200
        m = np.array([
            [int(x[2*i]), int(x[2*i+1])],
            [int(y[2*i]), int(y[2*i+1])]
        ], dtype="f8")
        t = np.array([int(x_t[i])+10000000000000, int(y_t[i])+10000000000000])
        inp = np.linalg.solve(m, t)

        if not all(map(is_int, inp)):
            # not all are integer
            continue

        cost = round(inp[0]) * 3 + round(inp[1])
        total_cost += cost

    print(total_cost)

if __name__ == "__main__":
    main()
    # 47662833404956 too low

    # test expected
    # (1) fail
    # (2) 459 236 326 669
    # (3) fail
    # (4) 416 082 282 329
    # 875 318 608 998

    # 73267584326867
