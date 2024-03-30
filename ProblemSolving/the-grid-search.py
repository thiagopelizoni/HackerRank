# https://www.hackerrank.com/challenges/the-grid-search/problem
import os

def gridSearch(G, P):
    for i in range(len(G) - len(P) + 1):
        for j in range(len(G[0]) - len(P[0]) + 1):
            if all(G[i + k][j:j + len(P[0])] == P[k] for k in range(len(P))):
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])
        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])
        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()
