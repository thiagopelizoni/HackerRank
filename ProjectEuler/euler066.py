# https://www.hackerrank.com/contests/projecteuler/challenges/euler066/problem
import math

def is_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def find_minimal_solution(D):
    m, d, a = 0, 1, int(math.sqrt(D))
    num1, num2 = 1, a
    den1, den2 = 0, 1

    while num2 * num2 - D * den2 * den2 != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (int(math.sqrt(D)) + m) // d

        num1, num2 = num2, a * num2 + num1
        den1, den2 = den2, a * den2 + den1

    return num2

def find_largest_minimal_solution(limit):
    max_D = 0
    max_minimal_solution = 0

    for D in range(2, limit + 1):
        if not is_square(D):
            solution = find_minimal_solution(D)
            if solution > max_minimal_solution:
                max_minimal_solution = solution
                max_D = D

    return max_D

if __name__ == "__main__":
    limit = int(input())
    answer = find_largest_minimal_solution(limit)
    print(answer)
