#  https://www.hackerrank.com/contests/projecteuler/challenges/euler006/
def sum_square_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))

    square_of_sum = sum(range(1, n + 1)) ** 2

    difference = abs(sum_of_squares - square_of_sum)

    return difference

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(sum_square_difference(n))
