#  https://www.hackerrank.com/contests/projecteuler/challenges/euler008/

def largest_product(n, k, num):
    max_product = 0
    for i in range(n - k + 1):
        product = 1
        for j in range(k):
            product *= int(num[i + j])
        max_product = max(max_product, product)
    return max_product

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        num = input()

        print(largest_product(n, k, num))
