#  https://www.hackerrank.com/contests/projecteuler/challenges/euler005/
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(smallest_multiple(n))
