#  https://www.hackerrank.com/contests/projecteuler/challenges/euler004/
def maior_palindromo(n):
    maior = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            produto = i * j

            if produto < maior:
                break

            if produto < n and str(produto) == str(produto)[::-1]:
                maior = produto
                break
    return maior

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(maior_palindromo(n))
