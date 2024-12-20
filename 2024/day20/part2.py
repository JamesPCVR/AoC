from collections import Counter

def find_2d(track_map:list[list[str]], look_for:str) -> tuple[int,int]:
    """look for a character in a 2d list"""
    for y, line in enumerate(track_map):
        try:
            x = line.index(look_for)
            return x, y
        except ValueError:
            continue
    return -1, -1

def get_2d(track_map:list[list[str]], coords:tuple[int,int]) -> str|int:
    """get item at position in track map"""
    x, y = coords
    return track_map[y][x]

def set_2d(track:list[list[int]], coords:tuple[int,int], value:int) -> None:
    """set value at coordinates"""
    x, y = coords
    track[y][x] = value

def layout_route(track_map:list[str]) -> tuple[list[list[int]],int]:
    """mark track as an incrementing series"""
    track = [[-1 for _ in line] for line in track_map]
    start = find_2d(track_map, "S")
    end = find_2d(track_map, "E")
    set_2d(track, start, 0)
    x, y = start
    neighbours = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    track_length = 0
    while (x, y) != end:
        for x_s, y_s in neighbours:
            x_c = x + x_s
            y_c = y + y_s
            if get_2d(track, (x_c, y_c)) != -1:
                continue
            if get_2d(track_map, (x_c, y_c)) != "#":
                x, y = x_c, y_c
                break
        track_length += 1
        set_2d(track, (x, y), track_length)
    return track, track_length

def add_coords(a:tuple[int,int], b:tuple[int,int]) -> tuple[int,int]:
    """add x and y values of coordinates."""
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y

def generate_points_lut(distance:int) -> list[tuple[int,int]]:
    """create diamond of point deltas"""
    points_lut = []
    for x in range(-distance, distance + 1):
        for y in range(-distance + abs(x), distance + 1 - abs(x)):
            points_lut.append(((x, y), abs(x) + abs(y)))
    return points_lut

def points_within_lut(track:list[list[int]], start:tuple[int,int], points_lut:list[tuple[tuple, int]]) -> set[tuple[int,int]]:
    """find all `"."` within linear distance of start and within bounds"""
    x_lim = len(track[0]) - 1
    y_lim = len(track) - 1
    free_points = set()
    for point_delta, weight in points_lut:
        point = add_coords(start, point_delta)
        if not 0 <= point[0] <= x_lim:
            continue
        if not 0 <= point[1] <= y_lim:
            continue
        if get_2d(track, add_coords(start, point_delta)):
            free_points.add((point, weight))
    return free_points

def cheats(track:list[list[int]], track_length:int) -> list[int]:
    """find all time saving by cheating once"""
    points_lut = generate_points_lut(20)
    savings = []
    start = find_2d(track, 0)
    next_pos = start
    for index in range(track_length+1):
        pos = next_pos
        neighbours = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for neighbour in neighbours:
            next_to = add_coords(pos, neighbour)
            ahead = get_2d(track, next_to)
            if ahead - 1 == index:
                next_pos = next_to
        for check, weight in points_within_lut(track, pos, points_lut):
            value = get_2d(track, check)
            bridge = value - weight
            if bridge <= index: # not saving time
                continue
            delta = bridge - index
            savings.append(delta)
    return savings

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        track_map = f.read().split("\n")

    track, length = layout_route(track_map)
    savings = cheats(track, length)

    saves_enough = 0
    for k, v in Counter(savings).items():
        if k >= 100:
            saves_enough += v

    print(saves_enough)

if __name__ == "__main__":
    main()
    # 1021490
