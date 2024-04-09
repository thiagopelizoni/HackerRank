# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
import os

def activityNotifications(expenditure, d):
    notifications = 0
    count = [0] * 201

    for i in range(d):
        count[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = 0
        if d % 2 == 0:
            first = second = None
            total = 0
            for j in range(201):
                total += count[j]
                if first is None and total >= d // 2:
                    first = j
                if second is None and total >= d // 2 + 1:
                    second = j
                    break
            median = (first + second) / 2
        else:
            total = 0
            for j in range(201):
                total += count[j]
                if total > d // 2:
                    median = j
                    break

        if expenditure[i] >= 2 * median:
            notifications += 1

        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
