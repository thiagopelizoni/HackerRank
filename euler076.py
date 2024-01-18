# https://www.hackerrank.com/contests/projecteuler/challenges/euler076/problem
MOD = 10**9 + 7

def counting_sommations(n):
    res = [0] * (n + 1)
    res[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            res[j] = (res[j] + res[j - i]) % MOD
    return res[n]

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(counting_sommations(n))

if __name__ == "__main__":
    main()