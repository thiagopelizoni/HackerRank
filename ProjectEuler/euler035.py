#  https://www.hackerrank.com/contests/projecteuler/challenges/euler035/
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def rotate_number(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(n):
    return all(is_prime(rot) for rot in rotate_number(n))

def sum_of_circular_primes_below(limit):
    return sum(n for n in range(2, limit) if is_circular_prime(n))

if __name__ == '__main__':
    n = int(input().strip())
    print(sum_of_circular_primes_below(n))
