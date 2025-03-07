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
    if (dp[n][visited] != -1) : return dp[n][visited] #탐색 한번 처리한 것은 확실하게 제외해주어야 한다
    #그렇게 하지 않으면 탐색을 햇음에도 불구하고 답이 안나와서 그대로 둔걸 나중에 다시중복 연산을하게 된다.
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
    
    for i in dp : print(i)

#0,0이라고 해서 반드시 return 값이 모든 탐색을 안한 것이 될 필요는 없다
#탐색과 결과 값은 다른것
#dfs(0,0)이라고 해서 그것의 return 값이 반드시 모든 것에 대한 탐색이 안되는 것은 아니다.
#dfs(0,0)이라도 그것이 모든 것에 대한 탐색의 결과 값을 뱉을 수도 있는 것
#0번 인간 아무것도 탐색 안했음 부터 시작하는 것이라는 의미일 뿐이지 이게 나중에 모든 탐색 값을 뱉을 수도 있는 것이다.
