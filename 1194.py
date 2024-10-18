import sys

rl = sys.stdin.readline

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
keys = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5}
doors = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5}
finalResult = sys.maxsize #이건 1번을 밟았을때 리프레시 해준다.

def BFS(key, i, j, step) :#BFS시작
    print("[key : {0}, i : {1}, j : {2}, step : {3}".format(bin(key), i, j,step))
    q = []; q.append([i, j])#BFS시작 
    step = 0
    while q :
        print(q)
        tmp = q.pop()
        step += 1
        for d in direction : 
            ni = tmp[0] + d[0]; nj = tmp[1] + d[1]
            if ni < 0 or N - 1 < ni or nj < 0 or nj > M - 1 or map[ni][nj] == '#' :#범위 밖으로 나가버리는 경우에는 다음 for문을 돌린다.
                continue
            map[ni][nj] = next
            if (next == '.') :
                DP[ni][nj][key] = min(DP[key][ni][nj], step)
                q.append([ni, nj])
            if (next in keys) :#key를 발견한 경우
                key = (key | keys.get(next))#기존 보유하고 있던 key를 업데이트 해주고
                BFS(key , ni, nj, step)#BFS를 다시 시작해 준다.
            if (next in doors) :#문을 발견한 경우
                if (key & doors.get(next)) :#key가 있으면 연다
                    DP[ni][nj][key] = min(DP[key][ni][nj], step)
                    q.append([ni][nj])
            if (next == '1') :#출구를 발견한 경우
                    DP[ni][nj][key] = min(DP[key][ni][nj], step)
                    finalResult = min(finalResult, step)
    return 0

N, M = map(int, rl().split())

# map 생성
map = [[*input()] for _ in range(0, N)]

for i in map :
    print(i)

start = [] 

# i에서 시작한다
for i in range(N) : 
    for j in range(M) :
        if map[i][j] == '0' :   
            start = [i, j]

DP = [[[sys.maxsize for _ in range(64)] for _ in range(N)] for _ in range(M)]

BFS(0, start[0], start[1], 0)

print(finalResult)