def sieve(n):
    multiples = set()
    primes = list()
    for i in range(2, n + 1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i ** 2, n + 1, i))
    return primes
