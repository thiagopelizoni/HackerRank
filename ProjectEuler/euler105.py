# https://www.hackerrank.com/contests/projecteuler/challenges/euler105/problem
# That's my attempt to solve but not passed on all test cases resulting in timeout
import itertools

def is_special_sum_set(s):
    s = sorted(s)
    for i in range(1, len(s) + 1):
        for subset in itertools.combinations(s, i):
            remaining_elements = set(s) - set(subset)
            for j in range(1, len(remaining_elements) + 1):
                for subset2 in itertools.combinations(remaining_elements, j):
                    if sum(subset) == sum(subset2) or (len(subset) > len(subset2) and sum(subset) <= sum(subset2)):
                        return 'NO'
    return 'YES'
    
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))
        answer = is_special_sum_set(a)
        print(answer)