#  https://www.hackerrank.com/contests/projecteuler/challenges/euler040/
def champernownes_constant(n):
    i = 1
    while True:
        n += -(9 * 10**(i - 1)) * i
        if n <= 0:
            n += (9 * 10**(i - 1)) * i
            break
        i += 1

    m = (n - 1) // i
    result = str(10**(i - 1) + m)[n - m * i - 1]
    return int(result)

def main():
    num_queries = int(input())
    for _ in range(num_queries):
        digits = input().split()
        product = 1
        for i in digits:
            product *= champernownes_constant(int(i))
        print(product)

if __name__ == "__main__":
    main()
