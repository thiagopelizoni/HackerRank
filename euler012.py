#  https://www.hackerrank.com/contests/projecteuler/challenges/euler012/
def count_divisors(n):
    divisors = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors += 2 if i * i != n else 1
    return divisors

def find_triangular_number(min_divisors):
    i = 1
    triangle_number = 1
    while True:
        if i % 2 == 0:
            count = count_divisors(i // 2) * count_divisors(i + 1)
        else:
            count = count_divisors(i) * count_divisors((i + 1) // 2)

        if count > min_divisors:
            return triangle_number

        i += 1
        triangle_number += i

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        print(find_triangular_number(n))
