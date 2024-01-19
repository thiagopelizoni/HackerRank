# https://www.hackerrank.com/contests/projecteuler/challenges/euler087/problem
import math
import bisect

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def main():
    big_N = 10**7
    N = int(math.sqrt(big_N))
    primes = sieve_of_eratosthenes(N)
    
    sum_list = set()
    
    for i in range(2, int(big_N ** 0.5) + 1):
        for j in range(2, int(big_N ** (1/3)) + 1):
            for k in range(2, int(big_N ** (1/4)) + 1):
                if primes[i] and primes[j] and primes[k]:
                    Sum = i**2 + j**3 + k**4
                    if Sum > big_N:
                        break
                    sum_list.add(Sum)
    
    sums = sorted(sum_list)
    
    num_queries = int(input())
    
    for _ in range(num_queries):
        n = int(input())
        print(bisect.bisect_right(sums, n))

if __name__ == "__main__":
    main()
