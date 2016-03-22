from math import sqrt

def sieve(n):
    primes = []
    primes.append(2)
    for i in range(3, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes

def isPrime(n):
    if n % 2 == 0:
        return False

    flag = True

    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break

    return flag
