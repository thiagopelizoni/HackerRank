# https://www.hackerrank.com/contests/projecteuler/challenges/euler254/problem
# TestCase 0 done only. All others I failed by timeout.

from math import factorial

def f(n):
    return sum(factorial(int(digit)) for digit in str(n))

def sf(n):
    return sum(int(digit) for digit in str(f(n)))

def g(i):
    n = 1
    while sf(n) != i:
        n += 1
    return n

def sg(i):
    return sum(int(digit) for digit in str(g(i)))

def calculate_sg_sum_modulo(n, m):
    return sum(sg(i) for i in range(1, n+1)) % m

q = int(input().strip())

queries = []
for _ in range(q):
    n, m = map(int, input().split())
    queries.append((n, m))

answer = [calculate_sg_sum_modulo(n, m) for n, m in queries]
[print(i) for i in answer]
