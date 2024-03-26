# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    obs_dict = {(r, c) for r, c in obstacles}

    # Directions: Up, Down, Left, Right, Upper Left, Upper Right, Lower Left, Lower Right
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    count = 0

    for d in directions:
        r, c = r_q + d[0], c_q + d[1]
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obs_dict:
            count += 1
            r, c = r + d[0], c + d[1]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()
