#  https://www.hackerrank.com/contests/projecteuler/challenges/euler002/
def soma_fibonacci_pares(limite):
    soma = 0
    a, b = 1, 1
    while True:
        a, b = b, a + b
        if b > limite:
            break
        if b % 2 == 0:
            soma += b
    return soma

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(soma_fibonacci_pares(n))
