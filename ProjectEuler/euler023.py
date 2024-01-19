#  https://www.hackerrank.com/contests/projecteuler/challenges/euler023/
def calculate_abundant_numbers(N):
    ns = [0, 0] + [1] * N

    for step in range(2, N // 2):
        for n in range(step * 2, N + 1, step):
            ns[n] += step

    for n in range(len(ns)):
        ns[n] = ns[n] > n

    return ns

def can_be_written_as_sum(ns, n):
    for i in range(12, n):
        if ns[i] and ns[n - i]:
            return True
    return False

def main():
    N = 10**5
    ns = calculate_abundant_numbers(N)

    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        result = "YES" if can_be_written_as_sum(ns, n) else "NO"
        print(result)

if __name__ == "__main__":
    main()
