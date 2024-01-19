#  https://www.hackerrank.com/contests/projecteuler/challenges/euler030/
def sum_of_nth_powers(n):
    def digit_powers(x):
        return sum(int(digit)**n for digit in str(x))

    limit = 9**n * n
    return sum(i for i in range(2, limit) if i == digit_powers(i))

if __name__ == '__main__':
    n = int(input().strip())
    print(sum_of_nth_powers(n))
