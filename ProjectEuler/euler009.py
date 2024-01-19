#  https://www.hackerrank.com/contests/projecteuler/challenges/euler009/

def special_pythagorean_triplet(n):
    max_product = -1
    for a in range(1, n // 3):
        num = (n**2 - 2 * n * a)
        denom = (2 * n - 2 * a)
        b =  num // denom
        c = n - a - b
        success = a**2 + b**2 == c**2
        if success:
            max_product = max(max_product, a * b * c)
    return max_product

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(special_pythagorean_triplet(n))
