# https://www.hackerrank.com/challenges/append-and-delete/problem
def appendAndDelete(s, t, k):
    common_prefix_length = 0
    for i, (char_s, char_t) in enumerate(zip(s, t)):
        if char_s != char_t:
            break
        common_prefix_length += 1

    operations_needed = len(s) + len(t) - 2 * common_prefix_length

    if operations_needed <= k and (k - operations_needed) % 2 == 0:
        return "Yes"
    
    if k >= len(s) + len(t):
        return "Yes"
    
    return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
