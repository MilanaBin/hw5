from src.hw5.prime_num import is_prime, primes, сalc_checksum, pipeline


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(29)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(100)


def test_generate_primes():
    primes_list = primes(1000)
    assert len(primes_list) == 1000
    assert primes_list[0] == 2
    assert primes_list[-1] == 7919


def test_calculate_checksum():
    assert сalc_checksum([]) == 0
    assert сalc_checksum([1]) == 113
    assert сalc_checksum([1, 2, 6, 24]) == 6012369


def test_pipeline():
    aprimes_list, checksum_value = pipeline(1000, 100)
    assert checksum_value == 7785816


if __name__ == "__main__":
    test_is_prime()
    test_generate_primes()
    test_calculate_checksum()
    test_pipeline()
