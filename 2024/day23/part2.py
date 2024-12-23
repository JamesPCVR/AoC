from typing import Generator

def connect(connections:dict[str,set[str]], a:str, b:str) -> None:
    """create one-way link from node a to b"""
    if a in connections:
        connections[a].add(b)
    else:
        connections[a] = {b}

def bron_kerbosch(
        connections:dict[str,set[str]],
        clique:set[str],
        potential:set[str],
        processed:set[str]
    ) -> Generator[list[set[str]],None,None]:
    """find all cliques in the graph using bron kerbosch algorithm"""
    if not potential and not processed:
        yield clique
    while potential:
        v = potential.pop()
        yield from bron_kerbosch(
            connections,
            clique.union({v}),
            potential.intersection(connections[v]),
            processed.intersection(connections[v])
        )
        processed.add(v)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        content = f.read().split("\n")

    connections = {}
    for line in content:
        node_a, node_b = line.split("-")
        connect(connections, node_a, node_b)
        connect(connections, node_b, node_a)

    cliques = list(bron_kerbosch(connections, set(), set(connections.keys()), set()))
    largest_clique = set()
    largest_clique_size = 0
    for clique in cliques:
        if len(clique) > largest_clique_size:
            largest_clique_size = len(clique)
            largest_clique = clique

    print(largest_clique)
    print(largest_clique_size)

    password = ",".join(sorted(largest_clique))
    print(password)

if __name__ == "__main__":
    main()
    # gt,ha,ir,jn,jq,kb,lr,lt,nl,oj,pp,qh,vy
        