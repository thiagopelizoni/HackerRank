# https://www.hackerrank.com/contests/projecteuler/challenges/euler052/problem

def has_same_digits(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))

def find_permuted_multiples(n, k):
    for candidate in range(10, n + 1):
        if all(has_same_digits(candidate, candidate * multiplier) for multiplier in range(2, k + 1)):
            multiples = " ".join(str(candidate * factor) for factor in range(1, k + 1))
            print(multiples)

if __name__ == '__main__':
    n, k = map(int, input().split())
    find_permuted_multiples(n, k)
