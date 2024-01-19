#  https://www.hackerrank.com/contests/projecteuler/challenges/euler043/
from itertools import permutations

def is_special_pandigital(n, primes):
    for i in range(len(n) - 3):
        substring = int(n[i+1:i+4])
        if substring % primes[i] != 0:
            return False
    return True

def sum_of_special_pandigitals(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    digits = ''.join(str(i) for i in range(n + 1))
    total_sum = 0
    for p in permutations(digits):
        pandigital = ''.join(p)
        if is_special_pandigital(pandigital, primes):
            total_sum += int(pandigital)
    return total_sum

if __name__ == '__main__':
    n = int(input().strip())
    print(sum_of_special_pandigitals(n))
