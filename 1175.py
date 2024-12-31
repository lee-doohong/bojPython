import sys

# 동서남북 
direction = {'east' : [0, -1], 'west' : [0, 1], 'south' : [1, 0], 'north' : [-1, 0]}
# 선언
rl = sys.stdin.readline

# input 입력 부분
[N, M] = list(map(int, rl().split()))
map = [[*input()] for _ in range(N)]
for i in range(N) : 
    for j in range(M) :
        if map[i][j] == 'S' : start_x, start_y = i, j

result_time = 0

# dfs 함수

def dfs(x, y, former_dir, dp, time, cnt) :
    dp[x][y] = time # 현재의 시간을 찍어준다

    if map[next_x][next_y] == 'C' :
        dp =  [[sys.maxsize for _ in range(M)] for _ in range(N)]
        dp[x][y] = time # 현재의 시간을 다시 찍어준다
        cnt += 1

        if cnt == 2 : result_time = min(result_time, time)


    for dir in direction :
        if dir != former_dir :
            next_x = x+direction[dir][0]; next_y = y+direction[dir][1]
            
            # 범위를 벗어나거나 민식이가 갈 수 없는 곳 이거나 현재 위치 + 1 보다 앞으로 갈 위치의 dp 값이 작거나 같은 경우
            # 현재 위치 + 1 보다 앞으로 갈 위치의 dp 값이 커야 된다(작으면 갱신하는 의미가 없어)
            if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1 or map[next_x][next_y] == '#' or dp[next_x][next_y] > dp[x][y] + 1 :
                continue
            
            else : dfs(next_x, next_y, dir, [[0 for _ in range(M)] for _ in range(N)], time + 1, cnt)

# main함수

if __name__ == "__main__" :
    dfs(start_x, start_y, None, [[sys.maxsize for _ in range(M)] for _ in range(N)], 1, 0)
    if result_time == 0 : print(-1)
    else : print(result_time)
