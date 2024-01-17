#  https://www.hackerrank.com/contests/projecteuler/challenges/euler045/

def triangular(n):
        return n * (n + 1) // 2

def pentagonal(n):
    return n * (3 * n - 1) // 2

def hexagonal(n):
    return n * (2 * n - 1)

def triangular_pentagonal_hexagonal(N, A, B):
    if A == 3 and B == 5:
        f1, f2 = triangular, pentagonal
    elif A == 5 and B == 6:
        f1, f2 = pentagonal, hexagonal
    else:
        return []

    answer = []
    i, j = 1, 1

    while True:
        num1 = f1(i)
        num2 = f2(j)

        while num1 < num2:
            i += 1
            num1 = f1(i)
            if num1 >= N:
                return answer

        while num2 < num1:
            j += 1
            num2 = f2(j)
            if num2 >= N:
                return answer

        if num1 == num2:
            answer.append(num1)
            i += 1
            j += 1

    return answer

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    answer = triangular_pentagonal_hexagonal(n, a, b)
    [print(i) for i in answer]
