# https://www.hackerrank.com/contests/projecteuler/challenges/euler083/problem
def min_path_sum(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = matrix[0][0]

    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    for _ in range(rows+cols-2):
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + matrix[i][j])
                if i < rows - 1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + matrix[i][j])
                if j < cols - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + matrix[i][j])

    return dp[-1][-1]

if __name__ == '__main__':
    t = int(input())
    matrix = []
    
    for i in range(t):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    answer = min_path_sum(matrix)
    print(answer)
