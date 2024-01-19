#  https://www.hackerrank.com/contests/projecteuler/challenges/euler031/
MOD = 10**9 + 7

def calculate_combinations(limit, multiples):
    ways_to_reach = [0] * (limit + 1)
    ways_to_reach[0] = 1

    for multiple in multiples:
        for current in range(limit - multiple + 1):
            ways_to_reach[current + multiple] += ways_to_reach[current]
            ways_to_reach[current + multiple] %= MOD

    return ways_to_reach

def main():
    max_limit = 10**5
    allowed_multiples = [1, 2, 5, 10, 20, 50, 100, 200]

    ways_to_reach_limit = calculate_combinations(max_limit, allowed_multiples)

    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        result = ways_to_reach_limit[n] % MOD
        print(result)

if __name__ == "__main__":
    main()
