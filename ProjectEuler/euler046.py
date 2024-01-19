#  https://www.hackerrank.com/contests/projecteuler/challenges/euler046/

def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, limit) if prime[p]]

def goldbach_other_conjecture(n):
    primes = sieve_of_eratosthenes(n)
    ways = 0

    for prime in primes:
        if prime > n:
            break

        square = ((n - prime) / 2)**0.5

        if square == int(square):
            ways += 1

    return ways

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(goldbach_other_conjecture(n))

