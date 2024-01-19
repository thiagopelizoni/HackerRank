# https://www.hackerrank.com/contests/projecteuler/challenges/euler088/problem
def compute_product_sum_numbers(k):
    def search(start, product, sum_, numbers):
        k_val = product - sum_ + numbers
        if k_val <= k:
            if product < product_sum[k_val]:
                product_sum[k_val] = product
            for i in range(start, (2 * k) // product + 1):
                search(i, product * i, sum_ + i, numbers + 1)

    product_sum = [float('inf')] * (k + 1)
    search(2, 1, 1, 1)
    return sum(set(product_sum[2:]))

if __name__ == '__main__':
    n = int(input().strip())
    answer = compute_product_sum_numbers(n)
    print(answer)
