#  https://www.hackerrank.com/contests/projecteuler/challenges/euler038/
def pandigital_multiples(n, k):
    def is_pandigital(num, k):
        num_str = str(num)
        if len(num_str) != k:
            return False
        return set(num_str) == set(str(i) for i in range(1, k + 1))

    multipliers = []
    for i in range(2, n):
        concatenated_product = ''
        for j in range(1, 10):
            concatenated_product += str(i * j)
            if len(concatenated_product) >= k:
                break
        if is_pandigital(int(concatenated_product), k):
            multipliers.append(i)
    return multipliers

if __name__ == '__main__':
    n, k = map(int, input().split())
    [print(i) for i in pandigital_multiples(n, k)]
