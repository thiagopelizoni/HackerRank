#  https://www.hackerrank.com/contests/projecteuler/challenges/euler034/
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def digit_factorials_sum(n):
    sum_result = 0
    for i in range(10, n):  # Starting from 10 as numbers below 10 are not sums
        sum_of_factorials = sum(factorial(int(digit)) for digit in str(i))
        if sum_of_factorials % i == 0:
            sum_result += i
    return sum_result

if __name__ == '__main__':
    n = int(input().strip())
    print(digit_factorials_sum(n))
