#  https://www.hackerrank.com/contests/projecteuler/challenges/euler001/
def calculate_sum(x):
    n3  = x // 3
    n5  = x // 5
    n15 = x // 15

    term_3  = 3 * (n3 * (n3 + 1) // 2)
    term_5  = 5 * (n5 * (n5 + 1) // 2)
    term_15 = 15 * (n15 * (n15 + 1) // 2)

    return term_3 + term_5 - term_15

def main():
    t = int(input())

    for _ in range(t):
        n = int(input()) - 1
        answer = calculate_sum(n)
        print(answer)

if __name__ == "__main__":
    main()
