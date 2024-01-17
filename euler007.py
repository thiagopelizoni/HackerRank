#  https://www.hackerrank.com/contests/projecteuler/challenges/euler007/
import math

def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

def nth_prime(n):
    limit = 125000 if n < 6 else int(n * (math.log(n) + math.log(math.log(n))))
    primes = sieve_of_eratosthenes(limit)

    return primes[n - 1]

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(nth_prime(n))
