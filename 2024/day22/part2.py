from typing import Generator

def mix(secret:int, num:int) -> int:
    """mix number into secret"""
    return secret ^ num

def prune(secret:int) -> int:
    """prune secret"""
    return secret % 16777216

def next_secret(secret:int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret

def secrets(initial_secret:int, num_secrets:int) -> Generator[int, None, None]:
    """generator of all secrets"""
    secret = initial_secret
    for _ in range(num_secrets):
        secret = next_secret(secret)
        yield secret

def generate_lut(price:tuple[int], pattern:tuple[int]) -> dict[tuple[int],int]:
    """generate lut of prices with patterns"""
    lut = {}
    for i in range(len(pattern) - 3):
        _slice = tuple(pattern[i:i+4])
        if _slice not in lut:
            _value = price[i+4]
            lut[_slice] = _value
    return lut

def patterns(bottom:int, top:int, nums:int) -> Generator[tuple[int],None,None]:
    """combinations of numbers"""
    pattern = [bottom] * nums
    yield tuple(pattern)
    while pattern != [top] * nums:
        pattern[0] += 1
        for i, p in enumerate(pattern):
            if p <= top:
                break
            pattern[i] = bottom
            if i+1 == nums:
                return
            pattern[i+1] += 1
        yield tuple(pattern)

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        starting_secrets = [int(num) for num in f.read().split("\n")]

    luts = []
    for start_secret in starting_secrets:
        last_price = start_secret % 10
        price = [last_price]
        delta = []
        for secret in secrets(start_secret, 2000):
            new_price = secret % 10
            delta.append(new_price - last_price)
            price.append(new_price)
            last_price = new_price
        luts.append(generate_lut(price, delta))

    totals = []
    for match in patterns(-9,9,4):
        total = 0
        for lut in luts:
            if match in lut:
                total += lut[match]
        if total != 0:
            totals.append(total)

    print(max(totals))

if __name__ == "__main__":
    main()
    # 1628
