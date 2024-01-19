# https://www.hackerrank.com/contests/projecteuler/challenges/euler069/problem

def sieve_of_eratosthenes():
    sieve = [True] * 10**3

    for i in range(0, 10**3, 2):
        sieve[i] = False
        
    for j in range(3, int(10**3) + 1, 2):
        if sieve[j]:
            for k in range(j * 2, 10**3, j):
                sieve[k] = False
                
    sieve[1] = False
    sieve[2] = True
    return sieve

def totient_maximum(n, primes):
    maximum = 1
    answer  = 0
    
    for i in range(len(primes)):
        if primes[i]:
            if maximum * i >= n:
                return maximum
            else:
                maximum *= i
                answer += i // (i - 1)

if __name__ == "__main__":
    t = int(input().strip())
    primes = sieve_of_eratosthenes()
    for _ in range(t):
        n = int(input().strip())
        print(totient_maximum(n, primes))
