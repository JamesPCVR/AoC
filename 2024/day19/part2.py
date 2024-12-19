from functools import lru_cache

@lru_cache(maxsize=None)
def try_match(towels:frozenset[str], pattern:str) -> int:
    """count number of ways to make pattern using available towels."""
    count = 0
    for towel in towels:
        if pattern == towel:
            count += 1
        if pattern.startswith(towel):
            count += try_match(towels, pattern.removeprefix(towel))
    return count

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        towels, patterns = f.read().split("\n\n", maxsplit=1)

    towels = frozenset(towels.split(", "))
    patterns = tuple(patterns.split("\n"))

    possible = sum(map(lambda p: try_match(towels, p), patterns))
    print(possible)

if __name__ == "__main__":
    main()
    # 843 too low
    # 623924810770264
