#  https://www.hackerrank.com/contests/projecteuler/challenges/euler014/

M = 1
lookup = []  # chain length for the number
longest = []  # max number producing the longest chain

def collatz(n: int) -> int:
    if n <= M and lookup[n] != 0:
        return lookup[n]

    c = collatz(n // 2 if n % 2 == 0 else n * 3 + 1) + 1
    if n <= M:
        lookup[n] = c

    return c

# Pre-compute up to the max N
def compute_collatz_numbers(n: int):
    global lookup, longest, M
    M = n
    lookup = [0] * (M + 1)
    longest = [0] * (M + 1)
    lookup[1] = longest[1] = 1
    max_number = max_chain = -1
    for i in range(1, M + 1):
        c = collatz(i)
        if max_chain <= c:
            max_chain = c
            max_number = i
        longest[i] = max_number

def main():
    num_tests = int(input())
    ns = [int(input()) for _ in range(num_tests)]
    max_n = max(ns)

    compute_collatz_numbers(max_n)

    [print(longest[n]) for n in ns]


if __name__ == "__main__":
    main()
