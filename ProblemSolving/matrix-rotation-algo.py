# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
def matrixRotation(matrix, r):
    rows, cols = len(matrix), len(matrix[0])
    layers = min(rows, cols) // 2

    for layer in range(layers):
        elements = []
        for col in range(layer, cols - layer):
            elements.append(matrix[layer][col])

        for row in range(layer + 1, rows - layer - 1):
            elements.append(matrix[row][cols - layer - 1])

        for col in range(cols - layer - 1, layer - 1, -1):
            elements.append(matrix[rows - layer - 1][col])

        for row in range(rows - layer - 2, layer, -1):
            elements.append(matrix[row][layer])

        r_mod = r % len(elements)
        elements = elements[r_mod:] + elements[:r_mod]

        idx = 0
        for col in range(layer, cols - layer):
            matrix[layer][col] = elements[idx]
            idx += 1

        for row in range(layer + 1, rows - layer - 1):
            matrix[row][cols - layer - 1] = elements[idx]
            idx += 1

        for col in range(cols - layer - 1, layer - 1, -1):
            matrix[rows - layer - 1][col] = elements[idx]
            idx += 1

        for row in range(rows - layer - 2, layer, -1):
            matrix[row][layer] = elements[idx]
            idx += 1

    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    m, n, r = map(int, input().split())

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
