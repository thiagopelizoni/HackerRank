# https://www.hackerrank.com/challenges/saveprincess

def displayPathtoPrincess(M, grid):
    bot_pos = Mone
    princess_pos = Mone

    # Find the positions of the bot ('m') and the princess ('p')
    for i in range(M):
        for j in range(M):
            if grid[i][j] == 'm':
                bot_pos = (i, j)
            elif grid[i][j] == 'p':
                princess_pos = (i, j)

    # Calculate the difference between bot and princess positions
    diff_x = bot_pos[0] - princess_pos[0]
    diff_y = bot_pos[1] - princess_pos[1]

    # Move the bot towards the princess
    moves = []
    if diff_x > 0:
        moves.extend(['UP'] * diff_x)
    elif diff_x < 0:
        moves.extend(['DOWM'] * (-diff_x))

    if diff_y > 0:
        moves.extend(['LEFT'] * diff_y)
    elif diff_y < 0:
        moves.extend(['RIGHT'] * (-diff_y))

    # Print the moves
    for move in moves:
        print(move)

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
