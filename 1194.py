import sys

rl = sys.stdin.readline

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
keys = {'a' : 1, 'b' : 2, 'c' : 4, 'd' : 8, 'e' : 16, 'f' : 32}
doors = {'A' : 1, 'B' : 2, 'C' : 4, 'D' : 8, 'E' : 16, 'F' : 32}
finalResult = sys.maxsize #이건 1번을 밟았을때 리프레시 해준다.

def BFS(key, i, j, step) :#BFS시작
    global finalResult
    q = []; q.append([i, j])#BFS시작 
    while q :
        tmp = q.pop()
        curstep = DP[key][tmp[0]][tmp[1]]
        for d in direction : 
            ni = tmp[0] + d[0]; nj = tmp[1] + d[1]
            if ni < 0 or N - 1 < ni or nj < 0 or nj > M - 1 or map[ni][nj] == '#' :#범위 밖으로 나가버리는 경우에는 다음 for문을 돌린다.
                continue
            next = map[ni][nj]
            if (next == '.' or next == '0') :
                if (curstep + 1 < DP[key][ni][nj]) : 
                    DP[key][ni][nj] = curstep + 1
                    q.append([ni, nj])
            if (next in keys) :#key를 발견한 경우
                if (curstep + 1 < DP[key][ni][nj]) : 
                    DP[key][ni][nj] = curstep + 1
                    tmpkey = (key | keys.get(next))#기존 보유하고 있던 key를 업데이트 해주고
                    DP[tmpkey][ni][nj] = curstep + 1
                    BFS(tmpkey , ni, nj, curstep + 1)#BFS를 다시 시작해 준다.
            if (next in doors) :#문을 발견한 경우
                if (key & doors.get(next)) :#key가 있으면 연다
                    if (curstep + 1 < DP[key][ni][nj]) : 
                        DP[key][ni][nj] = curstep + 1
                        q.append([ni, nj])
            if (next == '1') :#출구를 발견한 경우
                    if (curstep + 1 < DP[key][ni][nj]) : 
                        DP[key][ni][nj] = curstep + 1
                        finalResult = min(finalResult, DP[key][ni][nj])
    return 0

N, M = map(int, rl().split())

map = [[*input()] for _ in range(0, N)]

start = [] 

for i in range(N) : 
    for j in range(M) :
        if map[i][j] == '0' :   
            start = [i, j]

DP = [[[sys.maxsize for _ in range(M)] for _ in range(N)] for _ in range(64)]
DP[0][start[0]][start[1]] = 0
BFS(0, start[0], start[1], 0)

print(finalResult if finalResult != sys.maxsize else -1)

#이번에 확인한것 
# 1. 함부로 변수를 업데이트 하면 안된다. 특히 BFS나 DFS 또는 재귀와 같은 경우에는 변수 값을 업데이트 하면 예상치 못한 오류가 생긴다.
# 2. 전역변수 잘생각해주자. 함수내에서 전역 값을 바꿔주는 것이 있으면 반드시 global을 선언해줘야 안전하다
# 3. 파이썬은 다차원 함수 인ㄱ 경우 가장 큰걸 가장 마지막에 선언해준다.. 