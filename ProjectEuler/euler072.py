# https://www.hackerrank.com/contests/projecteuler/challenges/euler072/problem
def calculate_totient_numbers(limit):
    totient_lookup = [i for i in range(limit + 1)]

    for i in range(2, limit + 1):
        if totient_lookup[i] == i:
            for j in range(i, limit + 1, i):
                totient_lookup[j] -= totient_lookup[j] // i

    for i in range(3, limit):
        totient_lookup[i] += totient_lookup[i - 1]

    return totient_lookup

def main():
    t = int(input().strip())
    max_limit = 10 ** 6
    totient_lookup = calculate_totient_numbers(max_limit)

    for _ in range(t):
        n = int(input().strip())
        print(totient_lookup[n])

if __name__ == "__main__":
    main()
