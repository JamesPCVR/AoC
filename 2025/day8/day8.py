from itertools import combinations

import numpy as np
from numpy.typing import NDArray

FILENAME = "test.txt"
CONNECTIONS = 10

def dist(p1:NDArray, p2:NDArray):
    """Straight-line distance between two points."""
    return np.linalg.norm(p1-p2)

def pairs(arr:NDArray):
    """Compute the combinational pairings of an array."""
    return np.asarray(list(combinations(arr,2)))

def compute_distance(coords_arr:NDArray):
    """Compute straight-line distances between all pairs of points."""
    n = len(coords_arr)
    num_pairs = (n * (n-1)) // 2
    distances = np.zeros(num_pairs)
    pairings = pairs(coords_arr)
    for idx, (p1, p2) in enumerate(pairings):
        distances[idx] = dist(p1, p2)

    return distances

def pairs_sorted_closest(coords:list[tuple[int,int,int]]):
    """Get the pairs of coordinates sorted by their straight-line distance."""
    coords_arr = np.asarray(coords)
    distances = compute_distance(coords_arr)
    closest_indices = np.argsort(distances)
    closest_pairs = pairs(coords_arr)[closest_indices]
    return closest_pairs

def connect(
    p1:tuple[int,int,int],
    p2:tuple[int,int,int],
    circuits:list[set[tuple[int,int,int]]]
    ):
    """Connect two circuits together."""
    c1_i, c2_i = 0, 0
    for i, circuit in enumerate(circuits):
        if p1 in circuit:
            c1_i = i
        if p2 in circuit:
            c2_i = i

    # already connected
    if c1_i == c2_i:
        return

    # c2_i must be after c1_i
    if c2_i < c1_i:
        c1_i, c2_i = c2_i, c1_i

    c2 = circuits.pop(c2_i)
    circuits[c1_i].update(c2)

def part_1(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    coords:list[tuple[int,int,int]] = [
        tuple(map(int, line.strip().split(",", maxsplit=2)))
        for line in lines
    ]
    closest_pairs = pairs_sorted_closest(coords)[:CONNECTIONS]

    # connect the circuits
    circuits = [set((point,)) for point in coords]
    for pair in closest_pairs:
        p1, p2 = list(map(tuple, pair))
        connect(p1, p2, circuits)

    circuit_sizes = [len(circuit) for circuit in circuits]
    c = sorted(circuit_sizes, reverse=True)
    return c[0] * c[1] * c[2]

def part_2(): # pylint: disable= C0116
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()

    coords:list[tuple[int,int,int]] = [
        tuple(map(int, line.strip().split(",", maxsplit=2)))
        for line in lines
    ]
    closest_pairs = pairs_sorted_closest(coords)

    # connect the circuits
    circuits = [set((point,)) for point in coords]
    for pair in closest_pairs:
        p1, p2 = list(map(tuple, pair))
        connect(p1, p2, circuits)
        if len(circuits) == 1:
            return p1[0] * p2[0]

    return 0

if __name__ == "__main__":
    print(f"part 1: {part_1()}")
    print(f"part 2: {part_2()}")
