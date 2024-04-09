# https://www.hackerrank.com/challenges/countingsort4/problem
def countSort(arr):
    output = [[] for _ in range(100)]
    for i, (num, s) in enumerate(arr):
        idx = int(num)
        if i < len(arr) // 2:
            output[idx].append('-')
        else:
            output[idx].append(s)
    print(' '.join(s for group in output for s in group))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
