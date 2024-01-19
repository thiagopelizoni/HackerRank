#  https://www.hackerrank.com/contests/projecteuler/challenges/euler039/
import math

class PrimiterCalculator:
    def __init__(self):
        self.primiter = [0] * (5000000 + 1)
        self.ans = [0] * (5000000 + 1)

    def calculate_primiter(self):
        for m in range(1, 2001):
            for n in range(1, m):
                if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                    p = 2 * m * m + 2 * m * n
                    if p > 5000000:
                        continue
                    self.primiter[p] += 1
                    i = 2
                    while i * p <= 5000000:
                        self.primiter[i * p] += 1
                        i += 1

    def calculate_ans(self):
        self.ans[12] = 12
        for i in range(13, 5000001):
            if self.primiter[i] > self.primiter[self.ans[i - 1]]:
                self.ans[i] = i
            else:
                self.ans[i] = self.ans[i - 1]

    def run_queries(self):
        t = int(input())
        for _ in range(t):
            n = int(input())
            print(self.ans[n])

def main():
    calculator = PrimiterCalculator()
    calculator.calculate_primiter()
    calculator.calculate_ans()
    calculator.run_queries()

if __name__ == "__main__":
    main()
