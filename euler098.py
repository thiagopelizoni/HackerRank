# https://www.hackerrank.com/contests/projecteuler/challenges/euler098/problem
from collections import defaultdict
from math import isqrt

def largest_square_anagram(N):
    min_num = 10 ** (N - 1)
    max_num = 10 ** N
    min_square = isqrt(min_num)
    max_square = isqrt(max_num - 1)
    squares = [i**2 for i in range(min_square, max_square+1) if len(str(i**2)) == N]

    squares_dict = defaultdict(list)
    for square in squares:
        key = tuple(sorted(str(square)))
        squares_dict[key].append(square)

    largest_anagram_set = []
    for key, anagram_set in squares_dict.items():
        if len(anagram_set) > len(largest_anagram_set):
            largest_anagram_set = anagram_set

    return max(largest_anagram_set) if largest_anagram_set else None

n = int(input().strip())
answer = largest_square_anagram(n)
print(answer)
