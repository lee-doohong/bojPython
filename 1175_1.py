from collections import deque
import sys

direction = {1 : [0, 1], 2 : [0, -1], 3 : [1, 0], 4 : [-1, 0]}
[N, M] = list(map(int, sys.stdin.readline().split()))
map = [[*input()] for _ in range(N)]
list_C = []
result_time = float('inf')

for i in range(N) : 
    for j in range(M) :
        if map[i][j] == 'S' : start_x, start_y = i, j
        if map[i][j] == 'C' : list_C.append([i, j])

def change_bin(x, y) :
    return 1 if (list_C[0] == [x, y]) else 2

def bfs(x, y, former_dir, time, cnt, found_C) :
    global result_time
    
    dp = [[{1 : 0, 2 : 0, 3 : 0, 4 : 0, 0 : 0} for _ in range(M)] for _ in range(N)]
    dp[x][y][former_dir] = time
    queue = deque()
    queue.append([x, y, former_dir])

    while (queue) :
        x, y, former_dir = queue.popleft()
        if dp[x][y][former_dir] + 1 > result_time : continue        
        for dir in direction : 
            if former_dir == dir : continue
            next_x = x+direction[dir][0]; next_y = y+direction[dir][1]
            if 0 <= next_x <= N - 1 and 0 <= next_y <= M - 1 and map[next_x][next_y] != '#' and dp[next_x][next_y][dir] == 0 : 
                if map[next_x][next_y] == 'C' and (not found_C & change_bin(next_x, next_y)) : 
                    if (cnt == 1) : result_time = min(result_time, dp[x][y][former_dir] + 1)
                    else : bfs(next_x, next_y, dir, dp[x][y][former_dir] + 1, cnt + 1, change_bin(next_x, next_y))
                else :
                    dp[next_x][next_y][dir] = dp[x][y][former_dir] + 1
                    queue.append([next_x, next_y, dir])
                
if __name__ == "__main__" :
    bfs(start_x, start_y, 0, 0, 0, 0)
    if result_time == float('inf') : print(-1)
    else : print(result_time)