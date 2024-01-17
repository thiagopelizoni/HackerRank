# https://www.hackerrank.com/contests/projecteuler/challenges/euler053/problem
from math import comb

def count_combinations(N, K):
    count = 0
    for n in range(1, N + 1):
        for r in range(n + 1):
            if comb(n, r) > K:
                count += 1
    return count

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(count_combinations(n, k))
