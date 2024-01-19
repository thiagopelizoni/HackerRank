#  https://www.hackerrank.com/contests/projecteuler/challenges/euler016/
def power_digit_sum(n):
    """ Calculate 2^n and then sum its digits"""
    return sum(int(digit) for digit in str(2**n))

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(power_digit_sum(n))
