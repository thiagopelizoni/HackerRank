# https://www.hackerrank.com/challenges/correctness-invariant/problem

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key

if __name__ == "__main__":
    m = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    insertion_sort(ar)
    print(" ".join(map(str, ar)))