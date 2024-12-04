import sys
import math

rl = sys.stdin.readline
N = int(input())

D = [list(map(int, rl().split())) for _ in range(N)]

# 전체 숫자의 갯수
bit_num = int(math.pow(2, N)) - 1

# dp는 i는 누가 일을 한건지 m은 어떤일이 처리된건지
# 마지막에는 dp[N - 1][bit_num]을 출력하면 해결된다.
dp = [[0 for _ in range(bit_num)] for _ in range(N)] 

print(bit_num)

# n 현재 처리해야할 사람(10진수), m 현재까지 처리된 일(2진수), cost 현재까지 비용(10진수)
def dfs(n, m, cost) :
    print(f'[dfs] n : {n}, m :{m}, cost : {cost}')
    for i in range(N) :
        #처리안한일이 있으면 
        if (m & int(math.pow(2, i))) == 0 :
            # 현재까지의 값과 더해서 예상되는 값을 기존의 dp값과 비교해본다.
            # 현재까지 처리된 값
            work_progress = m | int(math.pow(2, i))
            print(f'[dfs] work_progress : {bin(work_progress)}')

            if cost + D[n][i] < dp[n][work_progress] or dp[n][work_progress] == 0:
                dp[n][work_progress] = cost + D[n][i]
                dfs(n+1, work_progress, dp[n][work_progress])
    print("dfs")

if __name__ == "__main__" :
    print("main")
    dfs(0, 0, 0)
    print(dp[N-1][bit_num])