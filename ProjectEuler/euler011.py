#  https://www.hackerrank.com/contests/projecteuler/challenges/euler011/

import math
import os
import random
import re
import sys

def max_product_in_grid(grid):
    max_product = 0
    grid_size = len(grid)

    # Check rows and columns
    for i in range(grid_size):
        for j in range(grid_size - 3):
            if i + 3 < grid_size:
                vertical_product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                max_product = max(max_product, vertical_product)

            horizontal_product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            max_product = max(max_product, horizontal_product)

    for i in range(grid_size - 3):
        for j in range(grid_size - 3):
            diag1_product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            diag2_product = grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j]
            max_product = max(max_product, diag1_product, diag2_product)

    return max_product

if __name__ == '__main__':
    grid = []

    for _ in range(20):
        grid.append(list(map(int, input().rstrip().split())))

    print(max_product_in_grid(grid))
