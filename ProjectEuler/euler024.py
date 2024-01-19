#  https://www.hackerrank.com/contests/projecteuler/challenges/euler024/
from itertools import permutations

def lexicographic_permutation(n):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    characters = 'abcdefghijklm'
    result = []
    n -= 1
    chars = list(characters)
    while chars:
        fact = factorial(len(chars) - 1)
        index = n // fact
        n %= fact
        result.append(chars.pop(index))

    return ''.join(result)

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(lexicographic_permutation(n))
