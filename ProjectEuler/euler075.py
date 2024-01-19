# https://www.hackerrank.com/contests/projecteuler/challenges/euler075/problem
import math
import bisect
import itertools

def build_lookup(limit):
    lookup = [0] * (limit + 1)
    
    for v, u in itertools.combinations(range(1, int((5 * 10 ** 6) ** 0.5) + 1, 2), 2):
        if u > v and math.gcd(u, v) == 1:
            s = u ** 2 + u * v
            for i in range(s, 5 * 10 ** 6 + 1, s):
                lookup[i] += 1
    
    return lookup

def find_unique_values(lookup):
    return [i for i in range(len(lookup)) if lookup[i] == 1]

def main():
    num_test_cases = int(input().strip())
    
    limit = 5 * 10 ** 6
    lookup = build_lookup(limit)
    unique_values = find_unique_values(lookup)
    
    for _ in range(num_test_cases):
        n = int(input().strip())
        count = bisect.bisect_right(unique_values, n)
        print(count)

if __name__ == "__main__":
    main()
