#  https://www.hackerrank.com/contests/projecteuler/challenges/euler041/
from itertools import permutations

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_pandigitals():
    pandigitals = []
    for i in range(1, 10):
        digits = [str(n) for n in range(1, i + 1)]
        pandigitals += [int(''.join(a)) for a in permutations(digits) if is_prime(int(''.join(a)))]
    return sorted(pandigitals, reverse=True)

def find_largest_pandigital(n, pandigitals):
    for i in pandigitals:
        if i <= n:
            return i
    return -1

if __name__ == '__main__':
    t = int(input().strip())
    pandigitals = generate_pandigitals()
    for _ in range(t):
        n = int(input().strip())
        answer = find_largest_pandigital(n, pandigitals)
        print(answer)
