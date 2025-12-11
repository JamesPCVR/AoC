Devices = dict[str,list[str]]

def get_devices(filename:str) -> Devices: # pylint: disable= C0116
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    devices = {}
    for line in lines:
        line_split = line.strip().split(" ")
        device = line_split[0][:-1]
        connected = line_split[1:]
        devices[device] = connected

    return devices

def depth_first_paths(start:str, target:str, devices:Devices):
    """The number of paths to a target in a digraph."""
    if start == target:
        return 1

    return sum(
        depth_first_paths(next_device, target, devices)
        for next_device in devices[start]
    )

def part_1(devices:Devices): # pylint: disable= C0116
    return depth_first_paths("you", "out", devices)

def depth_first_paths_limited(start:str, target:str, devices:Devices, limit:int=20):
    """The number of paths to a target in a digraph. Depth limited."""
    if limit == 0:
        return 0
    if start == target:
        return 1

    try:
        return sum(
            depth_first_paths_limited(next_device, target, devices, limit-1)
            for next_device in devices[start]
        )
    except KeyError:
        return 0

def part_2(devices:Devices): # pylint: disable= C0116
    p1 = depth_first_paths_limited("svr", "fft", devices, 11)
    p2 = depth_first_paths_limited("fft", "dac", devices, 16)
    p3 = depth_first_paths_limited("dac", "out", devices, 13)
    return p1 * p2 * p3

if __name__ == "__main__":
    dev = get_devices("in.txt")
    print(f"part 1: {part_1(dev)}")
    print(f"part 2: {part_2(dev)}")