# https://www.hackerrank.com/challenges/saveprincess2

def nextMove(n, r, c, grid):
    # Find the position of the princess ('p')
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_r, princess_c = i, j

    # Calculate the difference between bot and princess positions
    dr = r - princess_r
    dc = c - princess_c

    # Determine the next move based on the difference
    if dr > 0:
        return "UP"
    elif dr < 0:
        return "DOWN"
    elif dc > 0:
        return "LEFT"
    elif dc < 0:
        return "RIGHT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
