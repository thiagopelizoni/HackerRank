# https://www.hackerrank.com/challenges/winning-lottery-ticket/problem
import os

def winningLotteryTicket(tickets):
    # Count tickets by the set of unique numbers they contain
    counter = [0] * 1024  # 1024 = 2^10, for all possible combinations of 0-9
    for ticket in tickets:
        mask = 0
        for digit in set(ticket):  # unique digits to avoid repetition
            mask |= 1 << int(digit)
        counter[mask] += 1

    result = 0
    for i in range(1024):
        for j in range(i, 1024):
            if i | j == 1023:  # 1023 = binary 1111111111, which represents 0-9
                if i == j:
                    result += counter[i] * (counter[i] - 1) // 2
                else:
                    result += counter[i] * counter[j]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
