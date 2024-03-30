# https://www.hackerrank.com/challenges/3d-surface-area/problem
import os

def surfaceArea(A):
    H, W = len(A), len(A[0]) if A else (0, 0)
    area = 0

    for row in range(H):
        for column in range(W):
            area += 2
            area += A[row][column] if row == 0 else max(0, A[row][column] - A[row - 1][column])
            area += A[row][column] if row == H - 1 else max(0, A[row][column] - A[row + 1][column])
            area += A[row][column] if column == 0 else max(0, A[row][column] - A[row][column - 1])
            area += A[row][column] if column == W - 1 else max(0, A[row][column] - A[row][column + 1])
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)
    fptr.write(str(result) + '\n')
    fptr.close()
