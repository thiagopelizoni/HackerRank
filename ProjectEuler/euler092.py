# https://www.hackerrank.com/contests/projecteuler/challenges/euler092/problem
# That's my attempt to solve but not passed on all test cases
MODULO = 10**9 + 7

def square_digit_chain_end(limit):
    def square_of_digits(num):
        return sum(int(digit) ** 2 for digit in str(num))

    count = 0
    for i in range(1, limit):
        number = i
        while number != 1 and number != 89:
            number = square_of_digits(number)
        if number == 89:
            count += 1
    return count % MODULO

if __name__ == '__main__':
    K = int(input().strip())
    limit = 10**K
    answer = square_digit_chain_end(limit)
    print(answer)
