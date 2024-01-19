# https://www.hackerrank.com/contests/projecteuler/challenges/euler074/problem
import math

FACTORIAL_10 = [math.factorial(i) for i in range(10)]

mem = {}

circular_chains = {
    145: 1,
    169: 3,
    871: 2,
    872: 2,
    1454: 3,
    40585: 1,
    45361: 2,
    45362: 2,
    363601: 3,
}

def fac(n):
    return sum(FACTORIAL_10[int(num)] for num in str(n))

def get_chain(n):
    chain = []
    while n not in chain:
        chain.append(n)
        if n in mem:
            n = mem[n]
        else:
            i = fac(n)
            mem[n] = i
            n = i
    return chain

def find_numbers(N, L):
    res = []
    for i in range(N + 1):
        chain = circular_chains.get(i, None)
        if chain is None:
            s = "".join(sorted(str(i)))
            chain = mem[s] if s in mem else len(get_chain(i))
            mem[s] = chain
        if chain == L:
            res.append(i)
    return res

def main():
    num_cases = int(input().strip())
    inputs = [tuple(map(int, input().strip().split())) for _ in range(num_cases)]

    for N, L in inputs:
        res = find_numbers(N, L)
        if res:
            print(" ".join(map(str, res)))
        else:
            print(-1)

if __name__ == "__main__":
    main()
