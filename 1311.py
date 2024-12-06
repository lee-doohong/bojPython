import sys
import math

rl = sys.stdin.readline
N = int(input())

D = [list(map(int, rl().split())) for _ in range(N)]

bit_num = (1<<N) - 1

dp = [[-1 for _ in range(bit_num + 1)] for _ in range(N)] 

def dfs2(n, visited) : # n은 몇번째 사람에 대해서 현재 처리중인지를 하는 것임 # m은 현재까지 어디어디 처리했는지를 나타내줌
    # print('n : {0} visited : {1:0>3}'.format(n, bin(visited)[2:]))
    if (n == N) : return 0
    if (visited == bit_num) : return 0
    if (dp[n][visited] != -1) : return dp[n][visited]
    dp[n][visited] = sys.maxsize
    for i in range(N) : 
        if (visited & 1<<i) : continue
        # print(f'i : {i}')
        dp[n][visited] = min(dp[n][visited], dfs2(n+1, visited|1<<i) + D[n][i])
    
    return dp[n][visited]

if __name__ == "__main__" :
    # for i in dp :
    #     print(dp)

    print(dfs2(0, 0))
    
    # for i in dp : print(i)

    # for i in dp :
    #     print(dp)

    # print(dp[N-1][bit_num])

