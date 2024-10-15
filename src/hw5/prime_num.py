import random
import argparse


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, (x // 2) + 1):
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


def сalc_checksum(nums: list) -> int:
    checksum = 0
    for num in nums:
        checksum = (checksum + num) * 113
        checksum %= 10_000_007
    return checksum


def pipeline(count, seed):
    primes_list = primes(count)

    random.seed(100)
    random.shuffle(primes_list)

    checksum_value = сalc_checksum(primes_list)
    return primes_list, checksum_value


def main():
    parser = argparse.ArgumentParser(
        description="Программа для генерации простых чисел и вычисления контрольной суммы."
    )
    parser.add_argument("count", type=int, help="Количество простых чисел")
    parser.add_argument("seed", type=int, help="Seed для перемешивания")

    args = parser.parse_args()

    primes_list, result = pipeline(args.count, args.seed)

    print("Список простых чисел:")
    for prime in primes_list:
        print(prime)

    print(f"\nКонтрольная сумма: {result}")


if __name__ == "__main__":
    main()
