#  https://www.hackerrank.com/contests/projecteuler/challenges/euler020/
import math

def factorial_digit_sum(n):
    factorial_value = math.factorial(n)
    return sum(int(digit) for digit in str(factorial_value))

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(factorial_digit_sum(n))
