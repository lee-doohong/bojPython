import sys

# 동서남북 
direction = {'east' : [0, 1], 'west' : [0, -1], 'south' : [1, 0], 'north' : [-1, 0]}
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

result_time = sys.maxsize

dp_0 = [[{'east' : sys.maxsize, 'west' : sys.maxsize, 'south' : sys.maxsize, 'north' : sys.maxsize, 'start' : sys.maxsize} for _ in range(M)] for _ in range(N)]
dp_C1 = [[{'east' : sys.maxsize, 'west' : sys.maxsize, 'south' : sys.maxsize, 'north' : sys.maxsize} for _ in range(M)] for _ in range(N)]
dp_C2 = [[{'east' : sys.maxsize, 'west' : sys.maxsize, 'south' : sys.maxsize, 'north' : sys.maxsize} for _ in range(M)] for _ in range(N)]

def print_dp(dp) :
    if (not dp) : return dp
    return "\n" + "\n".join(str(s) for s in dp) + "\n"

def check_found_C(x, y, found_C, cnt) : # 방문했던 C가 아니면 True를 뱉는다.
    if (not cnt) : return True
    else : 
        return not ([x, y] == found_C)

def bfs(x, y, former_dir, time, cnt, found_C) :
    # print(f'[dfs] x : {x}, y : {y}, former_dir : {former_dir}, time : {time}, cnt : {cnt}')
    global result_time
    
    if cnt == 0 :
        dp = dp_0
    elif found_C == C1 :
        dp = dp_C1
    elif found_C == C2:
        dp = dp_C2

    dp[x][y][former_dir] = time
    queue = [] # queue에 넣을 부분([next_x, next_y, time+1, former_dir])

    while (queue) :
        x, y, time, former_dir = queue.pop()
        for dir in direction : 
            next_x = x+direction[dir][0]; next_y = y+direction[dir][1]
            if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1 or map[next_x][next_y] == '#' or dp[next_x][next_y][dir] < time + 1   : 
                # print("continue")
                continue

            if map[next_x][next_y] == 'C' and check_found_C(x, y, found_C, cnt) : 
                bfs(x, y, former_dir, time + 1, cnt, [next_x, next_y])
                        
            else : 
                # print(f'[dir] next_x : {next_x}, next_y : {next_y}')
                dfs(next_x, next_y, dir, time + 1, cnt, found_C)

    



    

# dfs 함수
def dfs(x, y, former_dir, time, cnt, found_C) :
    # print(f'[dfs] x : {x}, y : {y}, former_dir : {former_dir}, time : {time}, cnt : {cnt}')
    global result_time

    if map[x][y] == 'C' and check_found_C(x, y, found_C, cnt) :
        # print(f'C found!! x : {x}, y : {y}, cnt : {cnt}')
        if cnt == 1 :
            # print(f'C found!! result_time : {result_time}, time : {time}') 
            result_time = min(result_time, time)
            return
        else :
            found_C = [x, y] 
            dp_0[x][y][former_dir] = time
            cnt += 1

    if cnt == 0 :
        dp = dp_0
    elif found_C == C1 :
        dp = dp_C1
    elif found_C == C2:
        dp = dp_C2

    dp[x][y][former_dir] = time # 현재의 시간을 찍어준다

    for dir in direction :
        if dir != former_dir :
            # print(f' x : {x}, y : {y}, dir : {dir}')
            next_x = x+direction[dir][0]; next_y = y+direction[dir][1]
            if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1 or map[next_x][next_y] == '#' or dp[next_x][next_y][dir] < time + 1   :
                # print("continue")
                continue
            
            else : 
                # print(f'[dir] next_x : {next_x}, next_y : {next_y}')
                dfs(next_x, next_y, dir, time + 1, cnt, found_C)

# main함수
if __name__ == "__main__" :
    dfs(start_x, start_y, 'start', 0, 0, [])
    if result_time == sys.maxsize : print(-1)
    else : print(result_time)