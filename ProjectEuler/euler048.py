# https://www.hackerrank.com/contests/projecteuler/challenges/euler048/problem

def last_ten_digits_of_series(n):
    modulo = 10**10
    total = 0
    for i in range(1, n + 1):
        total += pow(i, i, modulo)
    return total % modulo

if __name__ == "__main__":
    n = int(input().strip())
    answer = last_ten_digits_of_series(n)
    print(answer)
