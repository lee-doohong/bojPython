import sys

# 동서남북 
direction = {1 : [0, 1], 2 : [0, -1], 3 : [1, 0], 4 : [-1, 0]}
# 선언
rl = sys.stdin.readline

# input 입력 부분
[N, M] = list(map(int, rl().split()))
map = [[*input()] for _ in range(N)]
list_C = []
for i in range(N) : 
    for j in range(M) :
        if map[i][j] == 'S' : start_x, start_y = i, j
        if map[i][j] == 'C' : list_C.append([i, j])

C1 = list_C[0]
C2 = list_C[1]

result_time = float('inf')

dp_0 = [[{1 : float('inf'), 2 : float('inf'), 3 : float('inf'), 4 : float('inf'), 0 : float('inf')} for _ in range(M)] for _ in range(N)]
dp_C1 = [[{1 : float('inf'), 2 : float('inf'), 3 : float('inf'), 4 : float('inf')} for _ in range(M)] for _ in range(N)]
dp_C2 = [[{1 : float('inf'), 2 : float('inf'), 3 : float('inf'), 4 : float('inf')} for _ in range(M)] for _ in range(N)]

def change_bin(x, y) :
    if (C1 == [x, y]) :
        return 1
    elif (C2 == [x, y]) :
        return 2
    else : return -1

# found_C 관련 아무것도 못발견 0b0 C1 발견 0b1 C2 발견 0b10
def bfs(x, y, former_dir, time, cnt, found_C) :
    global result_time
    
    if cnt == 0 :
        dp = dp_0
    elif found_C == 1 :
        dp = dp_C1
    elif found_C == 2:
        dp = dp_C2

    dp[x][y][former_dir] = time
    queue = [] # queue에 넣을 부분([next_x, next_y, time+1, former_dir])
    queue.append([x, y, time, former_dir])

    while (queue) :
        x, y, time, former_dir = queue.pop()
        dp[x][y][former_dir] = time
        for dir in direction : 
            if former_dir == dir :
                continue
            next_x = x+direction[dir][0]; next_y = y+direction[dir][1]
            if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1 or map[next_x][next_y] == '#' or dp[next_x][next_y][dir] <= time + 1 : 
                continue
            elif map[next_x][next_y] == 'C' and (not found_C & change_bin(next_x, next_y)) : 
                if (cnt == 1) :
                    result_time = min(result_time, time + 1)
                else : 
                    bfs(next_x, next_y, dir, time + 1, cnt + 1, change_bin(next_x, next_y))
            else :
                if time + 1 >= result_time : continue 
                else : queue.append([next_x, next_y, time + 1, dir])
                

# main함수
if __name__ == "__main__" :
    bfs(start_x, start_y, 0, 0, 0, 0)
    if result_time == float('inf') : print(-1)
    else : print(result_time)