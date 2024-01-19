# https://www.hackerrank.com/contests/projecteuler/challenges/euler077/problem
import random

def is_prime(n):
    if n in [2, 3, 5, 7]:
        return True
    
    d = n - 1
    s = 0
    
    while not d % 2:
        s += 1
        d = d // 2
    
    for _ in range(4):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        
        if x not in [1, n - 1]:
            active = True
            for r in range(s):
                if pow(x, 2 ** r, n) == n - 1:
                    active = False
                    break
            if active:
                return False
    return True

def generate_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * 2, limit + 1, num):
                sieve[multiple] = False
    return primes

def count_combinations(target, primes):
    combinations = [0] * (target + 1)
    combinations[0] = 1
    for prime in primes:
        for i in range(prime, target + 1):
            combinations[i] += combinations[i - prime]
    return combinations

def main():
    limit = 1000
    primes = generate_primes(limit)
    
    t = int(input())
    for _ in range(t):
        m = int(input().strip())
        combinations = count_combinations(m, primes)
        print(combinations[m])

if __name__ == "__main__":
    main()
