from itertools import combinations

def connect(connections:dict[str,set[str]], a:str, b:str) -> None:
    """create one-way link from node a to b"""
    if a in connections:
        connections[a].add(b)
    else:
        connections[a] = {b}

def find_triples(connections:dict[str,set[str]], start:str) -> set[frozenset[str]]:
    """find triple connections between start node and two satellites"""
    triples = set()
    for a, b in combinations(connections[start], 2):
        if a in connections[b]:
            triples.add(frozenset((start, a, b)))
    return triples

def node_starts_with(triple:frozenset[str], letter:str) -> bool:
    """check if triple has node beginning with letter"""
    for node in triple:
        if node[0] == letter:
            return True
    return False

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    connections = {}
    for line in content:
        node_a, node_b = line.split("-")
        connect(connections, node_a, node_b)
        connect(connections, node_b, node_a)

    all_triples = set()
    for start_node in connections:
        all_triples.update(find_triples(connections, start_node))

    with_t = set(filter(lambda tri: node_starts_with(tri, letter="t"), all_triples))
    print(len(with_t))

if __name__ == "__main__":
    main()
    # 1423
        