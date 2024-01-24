# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player_scores):
    dense_ranks = [1] * len(ranked)
    
    for i in range(1, len(ranked)):
        if ranked[i] == ranked[i - 1]:
            dense_ranks[i] = dense_ranks[i - 1]
        else:
            dense_ranks[i] = dense_ranks[i - 1] + 1

    player_ranks = [1] * len(player_scores)
    ranked_position = len(ranked) - 1
    
    for i in range(len(player_scores)):
        while ranked_position > -1:
            if ranked[ranked_position] > player_scores[i]:
                player_ranks[i] = dense_ranks[ranked_position] + 1
                break
            ranked_position -= 1
            
    return player_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
