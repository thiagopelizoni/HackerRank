# https://www.hackerrank.com/challenges/countingsort3/problem
def countingSort(arr):
    entries = [e[0] for e in arr]
    count = [entries.count(i) for i in range(100)]
    for i in range(1, 100):
        count[i] += count[i-1]
    print(' '.join(map(str, count)))
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr_i = input().strip().split(' ')
        arr_i[0] = int(arr_i[0])
        arr.append(arr_i)
        
    countingSort(arr)
