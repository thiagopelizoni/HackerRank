# https://www.hackerrank.com/contests/projecteuler/challenges/euler068/problem
from itertools import permutations

def generate_gon_ring(N, S):
    perms = permutations(range(1, 2*N + 1))
    solutions = []

    # Iterate over each permutation
    for perm in perms:
        inner = perm[:N]
        outer = perm[N:]

        # Check if the permutation can form a gon ring with the sum S
        if all(outer[i] + inner[i] + inner[(i+1) % N] == S for i in range(N)):
            # Find the solution with the correct starting point
            # The outer node with the smallest number should be first
            start = outer.index(min(outer))
            solution = [outer[start]]

            for i in range(N):
                index = (start + i) % N
                next_index = (start + i + 1) % N
                solution.extend([inner[index], inner[next_index]])

                if i < N - 1:
                    solution.append(outer[next_index])
            
            solutions.append(''.join(map(str, solution)))

    # Sort and filter unique solutions
    return sorted(set(solutions))

if __name__ == '__main__':
    N, S = map(int, input().split())
    answer = generate_gon_ring(N, S)
    [print(i) for i in answer]
