import re

SECONDS = 100

def is_in_limits(pos:tuple[int,int], limits:tuple[tuple[int,int],tuple[int,int]]) -> bool:
    x, y = pos
    x_limits, y_limits = limits
    if not (x_limits[0] <= x <= x_limits[1]):
        return False
    if not (y_limits[0] <= y <= y_limits[1]):
        return False
    return True

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        limits = tuple(map(int, f.readline().split(',')))
        content = f.read()
        r_p = [
            p.split(',') for p in re.findall(r"(?<=p=)-*\d+,-*\d+", content)
        ]
        robot_pos = [tuple(map(int, p)) for p in r_p]
        r_v = [
            v.split(',') for v in re.findall(r"(?<=v=)-*\d+,-*\d+", content)
        ]
        robot_vel = [tuple(map(int, v)) for v in r_v]

    new_positions = []

    for r_p, r_v in zip(robot_pos, robot_vel):
        d_p = tuple(map(lambda x: x*SECONDS, r_v))
        n_p = tuple(map(lambda x1, x2, lim: (x1 + x2)%lim, r_p, d_p, limits))
        new_positions.append(n_p)

    quardant_limits = (
        ((0, limits[0]//2-1), (0, limits[1]//2-1)),
        ((limits[0]//2+1, limits[0]-1), (0, limits[1]//2-1)),
        ((0, limits[0]//2-1), (limits[1]//2+1, limits[1]-1)),
        ((limits[0]//2+1, limits[0]-1), (limits[1]//2+1, limits[1]-1)),
    )

    quad_count = [0, 0, 0, 0]

    for pos in new_positions:
        for q, q_lim in enumerate(quardant_limits):
            if is_in_limits(pos, q_lim):
                quad_count[q] += 1

    safety = 1
    for q_c in quad_count:
        safety *= q_c

    print(safety)

if __name__ == "__main__":
    main()
    # 228690000
