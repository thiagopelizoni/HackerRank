# https://www.hackerrank.com/challenges/flatland-space-stations/problem
import os

def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = max(c[0], n - 1 - c[-1])
    for i in range(1, len(c)):
        max_distance = max(max_distance, (c[i] - c[i - 1]) // 2)
    return max_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    fptr.write(str(result) + '\n')
    fptr.close()
