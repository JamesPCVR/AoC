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

def main():
    with open("in.txt", "r", encoding="utf-8") as f:
        starting_secrets = [int(num) for num in f.read().split("\n")]

    total_2000 = 0
    for start_secret in starting_secrets:
        secret = start_secret
        for _ in range(2000):
            secret = next_secret(secret)
        total_2000 += secret

    print(total_2000)

if __name__ == "__main__":
    main()
    # 14392541715
