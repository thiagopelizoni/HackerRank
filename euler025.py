#  https://www.hackerrank.com/contests/projecteuler/challenges/euler025/
import math

def fibo(N):
    if N == 1:
        return 1
    phi = (1 + math.sqrt(5)) / 2
    return math.ceil((math.log(10) * (N - 1) + math.log(5) / 2) / math.log(phi))

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(fibo(n))
