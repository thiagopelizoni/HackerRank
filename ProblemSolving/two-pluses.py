# https://www.hackerrank.com/challenges/two-pluses/problem
import os

def judge(i, j, grid):
    cell = list(grid[i])[j]
    return cell

def change(indexes, grid):
    for index in indexes:
        i = index[0]
        j = index[1]
        row = list(grid[i])
        row[j] = 'B'
        grid[i] = ''.join(row)
    return grid

def find_max(grid):
    max_num = 0
    for row in range(n):
        for i in range(m):
            cell = judge(row, i, grid)
            if cell == 'G':
                local_max = 1
                distance = min(row, i, n-row-1, m-i-1)
                if distance != 0:
                    for j in range(distance):
                        if judge(row-(j+1), i, grid) == 'G' and judge(row+(j+1), i, grid) == 'G' and judge(row, i-(j+1), grid) == 'G' and judge(row, i+(j+1), grid) == 'G':
                            local_max += 4
                        else:
                            break
                    if local_max > max_num:
                        max_num = local_max
    return max_num

def twoPluses(grid):
    max_multiply = 0
    for row in range(n):
        for i in range(m):
            cell = judge(row, i, grid)
            if cell == 'G':
                local_max = 1
                local_index = [[row, i]]
                distance = min(row, i, n-row-1, m-i-1)
                local_grid = []
                for j in grid:
                    local_grid.append(j)
                local_grid = change(local_index, local_grid)
                local_sec_max = find_max(local_grid)
                if local_sec_max * local_max > max_multiply:
                    max_multiply = local_sec_max * local_max
                if distance != 0:
                    for j in range(distance):
                        if judge(row-(j+1), i, grid) == 'G' and judge(row+(j+1), i, grid) == 'G' and judge(row, i-(j+1), grid) == 'G' and judge(row, i+(j+1), grid) == 'G':
                            local_max += 4
                            local_index.append([row-(j+1), i])
                            local_index.append([row+(j+1), i])
                            local_index.append([row, i-(j+1)])
                            local_index.append([row, i+(j+1)])
                            local_grid = []
                            for j in grid:
                                local_grid.append(j)
                            local_grid = change(local_index, local_grid)
                            local_sec_max = find_max(local_grid)
                            if local_sec_max * local_max > max_multiply:
                                max_multiply = local_sec_max * local_max
                        else:
                            break
    return max_multiply

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
