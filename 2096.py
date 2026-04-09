from sys import stdin
import copy

def solution() :
    N = int(stdin.readline())
    roads = [list(map(int, stdin.readline().split())) for _ in range(N)]
    # dp_high = [[0] * 3 for _ in range(N)]
    # dp_low = [[0] * 3 for _ in range(N)]
    dp_high = copy.deepcopy(roads[0])
    dp_low = copy.deepcopy(roads[0])

    for i in range(1, N) :
        tmp_high = [0] * 3
        tmp_low = [0] * 3
        for j in range(3) :
            if j == 0 :
                tmp_high[j] = roads[i][j] + max(dp_high[0], dp_high[1])
                tmp_low[j] = roads[i][j] + min(dp_low[0], dp_low[1])
            elif j == 1 : 
                tmp_high[j] = roads[i][j] + max(dp_high[0], dp_high[1], dp_high[2])
                tmp_low[j] = roads[i][j] + min(dp_low[0], dp_low[1], dp_low[2])
            else : 
                tmp_high[j] = roads[i][j] + max(dp_high[1], dp_high[2])
                tmp_low[j] = roads[i][j] + min(dp_low[1], dp_low[2])

        dp_high = copy.deepcopy(tmp_high)
        dp_low = copy.deepcopy(tmp_low)

    print(f"{max(dp_high[0], dp_high[1], dp_high[2])} {min(dp_low[0], dp_low[1], dp_low[2])}")

if __name__ == "__main__" :
    solution()