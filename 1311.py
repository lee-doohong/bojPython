import sys
import math

rl = sys.stdin.readline
N = int(input())

D = [list(map(int, rl().split())) for _ in range(N)]

# 전체 숫자의 갯수
bit_num = int(math.pow(2, N)) - 1
# print(f'bit_num : {bin(bit_num)}')

# dp는 i는 누구까지 일이 처리된건지? j는 어떤일이 처리된건지
# 마지막에는 dp[N - 1][bit_num]을 출력하면 해결된다.
dp = [[sys.maxsize for _ in range(bit_num + 1)] for _ in range(N)] 
# for i in dp :
#     print(i)

# print(bit_num)
# print(dp[2][bit_num])

# n 현재 처리해야할 사람(10진수), m 현재까지 처리된 일(2진수), cost 현재까지 비용(10진수)
# bottom-up
def dfs(n, m, cost) :
    if (n == N or m == bit_num) : return
    # if (dp[n][m] != 0) : return dp[n][m]
    # print('[dfs] {1}번째 인간에 대해 탐색 중, 현재까지 처리된 일 : {0:0>3}, 현재까지 비용 : {2}'.format(bin(m)[2:], n+1, cost))
    for i in range(N) :
        #처리안한일이 있으면 
        if (m & int(math.pow(2, i))) == 0 :
            # print('[dfs] {1}번째 인간에 대해 탐색 중, 현재까지 처리된 일 : {0:0>3}, 현재까지 비용 : {2}, {3:0>3}번째 일을 탐색'.format(bin(m)[2:], n+1, cost, bin(i)[2:]))
            # 현재까지의 값과 더해서 예상되는 값을 기존의 dp값과 비교해본다.
            # 현재까지 처리된 값
            work_progress = m | int(math.pow(2, i))
            # print(f'[dfs] work_progress : {bin(work_progress)}, 10진수 {work_progress}')

            dp[n][work_progress] = math.min(dfs)
            if cost + D[n][i] < dp[n][work_progress]:
                dp[n][work_progress] = cost + D[n][i]
                dfs(n+1, work_progress, dp[n][work_progress])
    

#top-down 방식으로한다면..
# def dfs_top_down(n, m) :
#     if dp[n][m] != 0 : return dp[n][m]

def dfs2(n) : # n은 몇번째 사람에 대해서 현재 처리중인지를 하는 것임
    for i in range(bit_num) :
        # print(i)
        former_N = dp[n-1][i]
        if n == 0 :
            former_N = 0
        else :
            if former_N == sys.maxsize : continue

        for j in range(N) : 
            j_bin = int(math.pow(2, j))
            if(i & j_bin != 0) : continue
            dp[n][i | j_bin] = min(former_N + D[n][j], dp[n][i | j_bin])
            # print('dfs2[{0}] dp[{1}][{2}] = {3}'.format(n, n, bin(i|j), dp[n][i | j]))

if __name__ == "__main__" :
    # for i in dp :
    #     print(dp)

    for i in range(N) :
        dfs2(i)
    
    # for i in dp :
    #     print(dp)

    print(dp[N-1][bit_num])

