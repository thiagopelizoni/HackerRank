# https://www.hackerrank.com/challenges/bomber-man/problem
import os

def bomberMan(n, grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        return ['O' * len(grid[0])] * len(grid)

    def explode(gr):
        rows, cols = len(gr), len(gr[0])
        gri = [['O'] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if gr[i][j] == 'O':
                    gri[i][j] = '.'
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < rows and 0 <= y < cols:
                            gri[x][y] = '.'
        return gri

    grid = [list(row) for row in grid]
    return [''.join(row) for row in explode(explode(grid) if n % 4 == 1 else grid)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
