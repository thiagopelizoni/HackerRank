# https://www.hackerrank.com/contests/projecteuler/challenges/euler081/problem
def min_path_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    dp = [[float('inf')] * m for _ in range(n)]

    dp[0][0] = matrix[0][0]

    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + matrix[i][j])

            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + matrix[i][j])

    return dp[-1][-1]

if __name__ == '__main__':
    t = int(input())
    matrix = []
    for i in range(t):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    answer = min_path_sum(matrix)
    print(answer)
