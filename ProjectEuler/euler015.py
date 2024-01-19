#  https://www.hackerrank.com/contests/projecteuler/challenges/euler015/
def lattice_paths(n, m):
    grid = [[1 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[n][m] % 1000000007

if __name__ == '__main__':
    lenght = int(input().strip())

    for _ in range(lenght):
        params = input().split()
        n = int(params[0])
        m = int(params[1])
        print(lattice_paths(n, m))
