#  https://www.hackerrank.com/contests/projecteuler/challenges/euler027/
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_coefficients(limit):
    max_primes = 0
    max_a = 0
    max_b = 0

    for a in range(-limit, limit + 1):
        for b in range(-limit, limit + 1):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b

    return max_a, max_b

if __name__ == '__main__':
    n = int(input().strip())
    answer = find_coefficients(n)
    print(f"{answer[0]} {answer[1]}")
