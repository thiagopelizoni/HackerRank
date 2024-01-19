#  https://www.hackerrank.com/contests/projecteuler/challenges/euler042/
def is_triangular(n):
    if n < 1:
        return False
    return ((8 * n + 1) ** 0.5 - 1) % 2 == 0

def find_triangular_term(n):
    if is_triangular(n):
        return int(((-1 + (8 * n + 1) ** 0.5) / 2))
    else:
        return -1

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(find_triangular_term(n))
