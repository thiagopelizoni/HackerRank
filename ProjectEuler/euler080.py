# https://www.hackerrank.com/contests/projecteuler/challenges/euler080/problem
import decimal

def main():
    n = int(input().strip())
    p = int(input().strip())

    decimal.getcontext().prec = p + 4
    total = 0

    for i in range(2, n + 1):
        statement = int(i**0.5) != i**0.5
        if statement:
            sqrt_decimal = decimal.Decimal(i).sqrt()
            digits = str(sqrt_decimal)[:p + 1].replace('.', '')
            total += sum(map(int, digits))

    print(total)

if __name__ == "__main__":
    main()
