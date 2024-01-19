#  https://www.hackerrank.com/contests/projecteuler/challenges/euler018/
def max_path_sum(n):
    tr = []
    mx = []

    for i in range(n):
        tr.append(list(map(int, input().rstrip().split())))
        mx.append([0] * (i + 1))

    for j in range(n):
        mx[n - 1][j] = tr[n - 1][j]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            mx[i][j] = tr[i][j] + max(mx[i + 1][j], mx[i + 1][j + 1])

    print(mx[0][0])

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        max_path_sum(n)

if __name__ == "__main__":
    main()
