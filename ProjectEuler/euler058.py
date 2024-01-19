# https://www.hackerrank.com/contests/projecteuler/challenges/euler058/problem
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

def spiral_primes_percentage_below(N):
    side_length = 1
    total_primes = 0
    number = 1
    while True:
        for _ in range(4):
            side_length += 2
            for _ in range(4):
                number += side_length - 1
                if is_prime(number):
                    total_primes += 1
            if (total_primes / (2*side_length - 1)) * 100 < N:
                return side_length

if __name__ == '__main__':
    n = int(input().strip())
    print(spiral_primes_percentage_below(n))
