#  https://www.hackerrank.com/contests/projecteuler/challenges/euler003/
def maior_fator_primo(n):
    maior_fator = -1
    while n % 2 == 0:
        maior_fator = 2
        n //= 2

    limite = int(n ** 0.5) + 1
    intervalo = 2
    for i in range(3, limite, intervalo):
        while n % i == 0:
            maior_fator = i
            n //= i

    if n > 2:
        maior_fator = n

    return maior_fator

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(maior_fator_primo(n))
