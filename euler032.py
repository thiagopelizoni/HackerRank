#  https://www.hackerrank.com/contests/projecteuler/challenges/euler032/
def sum_of_pandigital_products(n):
    def is_pandigital(num):
        digits = str(num)
        return len(digits) == n and all(str(i) in digits for i in range(1, n + 1))

    products = set()
    for i in range(1, 10**(n // 2)):
        for j in range(1, 10**n):
            product = i * j
            combined = str(i) + str(j) + str(product)
            if len(combined) > n:
                break
            if len(combined) == n and is_pandigital(combined):
                products.add(product)

    return sum(products)

if __name__ == '__main__':
    n = int(input().strip())
    print(sum_of_pandigital_products(n))
