# https://www.hackerrank.com/contests/projecteuler/challenges/euler063/problem
N = int(input().strip())

def has_n_digits(number, n):
    return len(str(number)) == n

nth_powers_with_n_digits = []

upper_limit = 10**(1 / N) * 10

for i in range(1, int(upper_limit)):
    nth_power = i**N
    if has_n_digits(nth_power, N):
        nth_powers_with_n_digits.append(nth_power)

for num in nth_powers_with_n_digits:
    print(num)
