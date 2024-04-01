# https://www.hackerrank.com/challenges/almost-sorted/problem
def almostSorted(arr):
    index_list = [i for i, (x, y) in enumerate(zip(arr, sorted(arr))) if x != y]

    if len(index_list) == 2:
        print('yes')
        print(f'swap {index_list[0] + 1} {index_list[1] + 1}')
    elif len(index_list) > 2:
        sub_list = arr[index_list[0]:index_list[-1] + 1]
        if sub_list == sorted(sub_list, reverse=True):
            print('yes')
            print(f'reverse {index_list[0] + 1} {index_list[-1] + 1}')
        else:
            print('no')
    else:
        print('no')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
