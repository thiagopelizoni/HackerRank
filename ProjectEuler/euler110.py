# https://www.hackerrank.com/contests/projecteuler/challenges/euler110/problem
# That's my attempt to solve but not passed on all test cases resulting in timeout

def primes_up_to(n):
    """Sieve of Eratosthenes"""
    sieve = [True] * (n+1)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]

def num_divisors(n):
    """Return the number of divisors of n"""
    prime_divisors = primes_up_to(int(n**0.5) + 1)
    divisors_count = 1
    for p in prime_divisors:
        if n % p == 0:
            count = 1
            while n % p == 0:
                n //= p
                count += 1
            divisors_count *= count
    if n > 1:
        divisors_count *= 2
    return divisors_count

def find_least_n(X):
    n = 4
    while True:
    
        if (num_divisors(n**2) + 1) // 2 >= X:
            return n
        n += 1

n = int(input())
print(find_least_n(n))
