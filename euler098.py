# https://www.hackerrank.com/contests/projecteuler/challenges/euler098/problem
# That's my attempt to solve but not passed on all test cases
from math import sqrt

def are_anagrams(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))
        
def largest_square_anagram(N):
    max_square = int(sqrt(10**N - 1))
    min_square = int(sqrt(10**(N - 1)))
    
    squares = [i**2 for i in range(min_square, max_square+1)]
    sorted_squares = sorted(squares, key=lambda x: sorted(str(x)))
    
    largest_anagram_square = 0
    current_max_length = 0

    for i in range(len(sorted_squares) - 1):
        anagram_group = [sorted_squares[i]]
        while i + 1 < len(sorted_squares) and are_anagrams(sorted_squares[i], sorted_squares[i + 1]):
            anagram_group.append(sorted_squares[i + 1])
            i += 1

        if len(anagram_group) > current_max_length:
            current_max_length = len(anagram_group)
            largest_anagram_square = max(anagram_group)
        elif len(anagram_group) == current_max_length:
            largest_anagram_square = max(largest_anagram_square, max(anagram_group))

    return largest_anagram_square

n = int(input().strip())
answer = largest_square_anagram(n)
print(answer)
