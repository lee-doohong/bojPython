import sys

# 동(1)서(2)남(3)북(4)
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

result_time = sys.maxsize

#dp[0 = 무방문, 1 = C1방문, 2 = C2방문][N][M] = {direction : time}
dp = [[[{1 : sys.maxsize, 2 : sys.maxsize, 3 : sys.maxsize, 4 : sys.maxsize, 0 : sys.maxsize} for _ in range(M)] for _ in range(N)] for _ in range(3)]

def check_found_C(x, y, found_C, cnt) : # 방문했던 C가 아니면 True를 뱉는다.
    if (not cnt) : return True
    else : 
        return not ([x, y] == found_C)

def bfs() :
    global result_time
    global dp

    dp[0][start_x][start_y][0] = 0
    queue = [] # queue에 넣을 부분([cnt, next_x, next_y, time+1, former_dir, found_C])
    queue.append([0, start_x, start_y, 0, 0, []])

    while (queue) :
        cnt, x, y, time, former_dir, found_C = queue.pop()

        if (found_C == C1) : num = 1
        elif (found_C == C2) : num = 2
        else : num = 0 
        
        dp[num][x][y][former_dir] = time
        
        for dir in direction : 
            next_x = x+direction[dir][0]; next_y = y+direction[dir][1]
            if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1 or map[next_x][next_y] == '#' or dp[num][next_x][next_y][dir] <= time + 1 or former_dir == dir  : 
                continue
            elif map[next_x][next_y] == 'C' and check_found_C(next_x, next_y, found_C, cnt) : # 아직 발견하지 못한 C를 찾았다면
                if (cnt == 1) :
                    result_time = min(result_time, time + 1)
                else :     
                    queue.append([cnt + 1, next_x, next_y, time + 1, dir, [next_x, next_y]])
            else : 
                queue.append([cnt, next_x, next_y, time + 1, dir, found_C])

# main함수
if __name__ == "__main__" :
    bfs()
    if result_time == sys.maxsize : print(-1)
    else : print(result_time)