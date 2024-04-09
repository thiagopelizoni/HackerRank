# https://www.hackerrank.com/challenges/lilys-homework/problem
import os

def lilysHomework(arr):
    def countSwaps(arr):
        n = len(arr)
        arrpos = list(enumerate(arr))
        arrpos.sort(key=lambda it: it[1])
        vis = {i: False for i in range(n)}
        ans = 0
        for i in range(n):
            if vis[i] or arrpos[i][0] == i:
                continue
            cycle_size = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = arrpos[j][0]
                cycle_size += 1
            if cycle_size > 0:
                ans += (cycle_size - 1)
        return ans

    return min(countSwaps(arr[:]), countSwaps(arr[::-1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
