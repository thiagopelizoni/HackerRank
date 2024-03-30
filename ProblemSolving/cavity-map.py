# https://www.hackerrank.com/challenges/cavity-map/problem
import os

def cavityMap(grid):
    n = len(grid)
    grid = [list(row) for row in grid]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] > max(grid[i - 1][j], grid[i][j - 1], grid[i + 1][j], grid[i][j + 1]):
                grid[i][j] = 'X'

    return [''.join(row) for row in grid]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
