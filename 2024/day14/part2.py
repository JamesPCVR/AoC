import re
from PIL import Image

OUTPUT = ".\\out\\"

def create_tiles(size:tuple[int,int], robot_pos:list[tuple[int,int]]) -> list[list[str]]:
    """create a tilemap of `.` and `#`."""
    tiles = [list("." * size[0]) for _ in range(size[1])]
    for x, y in robot_pos:
        tiles[y][x] = "#"
    return tiles

def create_image(tiles:list[list[str]], name:str) -> None:
    x_lim = len(tiles[0])
    y_lim = len(tiles)
    img = Image.new('1', (x_lim,y_lim), "black")
    pixels = img.load()
    for i, line in enumerate(tiles):
        for j, tile in enumerate(line):
            pixels[j,i] = 1 if tile == '#' else 0

    img.save(OUTPUT+name+".png")

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

    seconds = 0
    while seconds < 10000:
        for i, (r_p, r_v) in enumerate(zip(robot_pos, robot_vel)):
            n_p = tuple(
                map(lambda x1, x2, lim: (x1 + x2)%lim, r_p, r_v, limits)
            )
            robot_pos[i] = n_p

        seconds += 1
        tiles = create_tiles(limits, robot_pos)
        create_image(tiles, str(seconds))

if __name__ == "__main__":
    main()
    # 30000 too high
    # 10000 too high
    # 7093
