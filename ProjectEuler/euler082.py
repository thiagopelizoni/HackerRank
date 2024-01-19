# https://www.hackerrank.com/contests/projecteuler/challenges/euler082/problem
t = int(input())
matrix = []

for i in range(t):
    row = list(map(int, input().split()))
    matrix.append(row)

# Define the dimensions of the matrix
rows, cols = len(matrix), len(matrix[0])

# Initialize the cost matrix with infinity values
cost = [[float('inf')]*cols for _ in range(rows)]

# Set the first column of the cost matrix to be the same as the input matrix
for i in range(rows):
    cost[i][0] = matrix[i][0]

# Compute the minimum path sum
for col in range(1, cols):
    # Update the cost of reaching each cell from the left
    for row in range(rows):
        cost[row][col] = min(cost[row][col], cost[row][col-1] + matrix[row][col])

    # Propagate the minimum cost upwards
    for row in range(1, rows):
        cost[row][col] = min(cost[row][col], cost[row-1][col] + matrix[row][col])

    # Propagate the minimum cost downwards
    for row in range(rows-2, -1, -1):
        cost[row][col] = min(cost[row][col], cost[row+1][col] + matrix[row][col])

# The minimum path sum is the minimum value in the last column of the cost matrix
min_path_sum = min(cost[row][-1] for row in range(rows))
print(min_path_sum)
