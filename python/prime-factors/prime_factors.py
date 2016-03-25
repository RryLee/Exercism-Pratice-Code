LIMIT = 1000000

def prime_factors(n):
    def sieve(n):
        multiples = set()
        for i in range(2, n + 1):
            if i not in multiples:
                yield i
                multiples.update(range(i ** 2, n + 1, i))
    factors = []
    if n != 1:
        for prime in sieve(LIMIT):
            if n > 1:
                while n % prime == 0:
                    n /= prime
                    factors.append(prime)
            else:
                break

    return factors

print prime_factors(6)
