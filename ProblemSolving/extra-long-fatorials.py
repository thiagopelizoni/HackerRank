# https://www.hackerrank.com/challenges/extra-long-factorials/problem
def extraLongFactorials(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

if __name__ == '__main__':
    n = int(input().strip())

    answer = extraLongFactorials(n)
    print(answer)
