# https://www.hackerrank.com/contests/projecteuler/challenges/euler057/problem

def calculate_sqrt2_expansions(N):
    iterations_with_more_numerators = []

    # Starting with the second iteration (first is trivially 1/1)
    num, den = 3, 2

    for i in range(2, N + 1):
        num, den = num + 2 * den, num + den

        if len(str(num)) > len(str(den)):
            iterations_with_more_numerators.append(i)

    return iterations_with_more_numerators

if __name__ == '__main__':
    n = int(input().strip())
    answer = calculate_sqrt2_expansions(n)
    [print(i) for i in answer]
