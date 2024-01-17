#  https://www.hackerrank.com/contests/projecteuler/challenges/euler010/

import math
import os
import random
import re
import sys

def sieve_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for m in range(i * i, limit + 1, i):
                sieve[m] = False
    return sieve

def calculate_primes(limit):
    sieve = sieve_eratosthenes(limit)
    primes = [i for i in range(limit + 1) if sieve[i]]
    return primes

def calculate_sums(primes):
    sums = dict()
    s = 0
    for prime in primes:
        s += prime
        sums[prime] = s
    return sums

def main():
    limit  = 10**6
    primes = calculate_primes(limit)
    sums   = calculate_sums(primes)

    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        while n > 1:
            if n in sums:
                print(sums[n])
                break
            n -= 1

if __name__ == "__main__":
    main()
