#  https://www.hackerrank.com/contests/projecteuler/challenges/euler028/
def calculate_sum_of_squares(n):
    if n == 1:
        return 1

    total = 1

    x = (n - 1) // 2
    total += (n * (n + 1) * (2 * n + 1) // 6 - 1 - 4 * (x * (x + 1) * (2 * x + 1) // 6)) * 4 - 6 * (x) * (x + 1)

    return total

def main():
    num_cases = int(input())

    for _ in range(num_cases):
        n = int(input())
        result = calculate_sum_of_squares(n) % (10**9 + 7)
        print(result)

if __name__ == "__main__":
    main()
