#  https://www.hackerrank.com/contests/projecteuler/challenges/euler044/

import math

def pentagonal_number(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(p):
    root = math.sqrt(1 + 24 * p)
    return root.is_integer() and (root + 1) % 6 == 0

def main():
    n, k = map(int, input().strip().split())
    for i in range(k + 1, n):
        difference = pentagonal_number(i) - pentagonal_number(i - k)
        count = pentagonal_number(i) + pentagonal_number(i - k)
        if is_pentagonal(difference) or is_pentagonal(count):
            print(pentagonal_number(i))

if __name__ == "__main__":
    main()
