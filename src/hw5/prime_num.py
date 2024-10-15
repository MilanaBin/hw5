import random

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


def primes(count: int) -> list:
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def checksum(nums: list) -> int:
    checksum = 0
    for num in nums:
        checksum = (checksum + num) * 113
        checksum %= 10_000_007
    return checksum


def pipeline() -> int:
    primes_list = primes(1000)

    random.seed(100)
    random.shuffle(primes_list)

    checksum = checksum(primes_list)
    return checksum


if __name__ == "__main__":
    result = pipeline()
    print(f"Контрольная сумма: {result}")
