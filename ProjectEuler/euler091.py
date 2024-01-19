# https://www.hackerrank.com/contests/projecteuler/challenges/euler091/problem
def count_right_triangles_corrected(max_coord):
    count = 0
    for x1 in range(max_coord + 1):
        for y1 in range(max_coord + 1):
            if x1 == 0 and y1 == 0:
                continue
            for x2 in range(max_coord + 1):
                for y2 in range(max_coord + 1):
                    if x2 == 0 and y2 == 0:
                        continue
                    if x1 == x2 and y1 == y2:
                        continue

                    # Check if the triangle is right-angled
                    dot_product1 = x1 * x2 + y1 * y2
                    dot_product2 = x1 * (x2 - x1) + y1 * (y2 - y1)
                    dot_product3 = x2 * (x2 - x1) + y2 * (y2 - y1)
                    if dot_product1 == 0 or dot_product2 == 0 or dot_product3 == 0:
                        count += 1

    return count // 2

if __name__ == '__main__':
    n = int(input().strip())
    answer = count_right_triangles_corrected(n)
    print(answer)

