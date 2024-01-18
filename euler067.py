# https://www.hackerrank.com/contests/projecteuler/challenges/euler067/problem
def find_maximum_total_in_triangle(triangle):
    num_rows = len(triangle)

    for row in range(num_rows - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

    return triangle[0][0]

def main():
    num_test_cases = int(input().strip())

    for _ in range(num_test_cases):
        num_rows = int(input().strip())
        triangle = []

        for _ in range(num_rows):
            row_values = list(map(int, input().strip().split()))
            triangle.append(row_values)

        max_total = find_maximum_total_in_triangle(triangle)
        print(max_total)

if __name__ == "__main__":
    main()
